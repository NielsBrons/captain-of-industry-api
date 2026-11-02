"""Offline standalone documentation checks; never contacts the game."""
import json
from pathlib import Path
import re
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


def sections(text, level):
    """Index headings at one level without allowing duplicate entries."""
    entries = {}
    for entry in re.split(r'^' + '#' * level + r' ', text, flags=re.M)[1:]:
        name, body = entry.split('\n', 1)
        assert name not in entries, ('duplicate heading', name)
        entries[name] = body
    return entries


def main():
    # Only the standalone documentation and its evidence are in scope.
    artifacts = [p for p in ROOT.iterdir() if p.is_file()]
    for directory in ('docs', 'discovery', 'tools'):
        artifacts.extend(p for p in (ROOT / directory).rglob('*') if p.is_file())
    files = [p for p in artifacts if p.suffix == '.json']
    for file in files:
        json.loads(file.read_text())
    routes = json.loads((ROOT / 'discovery/routes.json').read_text())
    commands = json.loads((ROOT / 'discovery/commands.json').read_text())
    assert len(routes) == 12
    assert len({(r['method'], r['path']) for r in routes}) == 12
    assert len(commands) == len({c['type'] for c in commands}) == 240
    constructor_count = sum(len(c['constructors']) for c in commands)
    assert constructor_count == 244
    endpoints = sections((ROOT / 'docs/endpoints.md').read_text(), 2)
    command_doc = sections((ROOT / 'docs/commands.md').read_text(), 2)
    for route in routes:
        key = route['method'] + ' ' + route['path']
        assert key in endpoints, key
        body = endpoints[key]
        assert 'Advertised stage: `' + route['stage'] + '`.' in body, key
        for param in route['params']:
            assert '`' + param['name'] + '`' in body, (key, param['name'])
    for command in commands:
        name = command['type']
        assert name in command_doc, name
        body = command_doc[name]
        assert 'Namespace: `' + command['namespace'] + '`.' in body, name
        assert 'Advertised result: `' + command['result'] + '`.' in body, name
        if command['description']:
            assert command['description'] in body, name
        constructors = sections(body, 3)
        assert len(constructors) == len(command['constructors']), name
        for index, ctor in enumerate(command['constructors'], 1):
            ctor_body = constructors['Constructor ' + str(index)]
            for param in ctor['params']:
                signature = '- `' + param['name'] + '`: game type `' + param['type'] + '`.'
                assert signature in ctor_body, (name, index, param['name'])
                # Check metadata within its own parameter, not another overload.
                param_body = ctor_body.split(signature, 1)[1].split('\n- `', 1)[0]
                if 'json' in param:
                    assert 'JSON hint: `' + param['json'] + '`.' in param_body, (name, param)
                if 'default' in param:
                    default = json.dumps(param['default'], ensure_ascii=False)
                    assert 'Default: `' + default + '`.' in param_body, (name, param)
                if param.get('description'):
                    assert param['description'] in param_body, (name, param)
                extra = {k: v for k, v in param.items()
                         if k not in ('name', 'type', 'json', 'default', 'description')}
                if extra:
                    assert json.dumps(extra, ensure_ascii=False) in param_body, (name, param)
    guide = (ROOT / 'docs/command-guide.md').read_text()
    guide_by_type = sections(guide, 3)
    assert set(guide_by_type) == {c['type'] for c in commands}
    for command in commands:
        name = command['type']
        body = guide_by_type[name]
        assert len(body.split()) >= 30, ('missing explanation', name)
        assert '(commands.md#' + name.lower() + ')' in body, name
        for ctor in command['constructors']:
            for param in ctor['params']:
                assert '`' + param['name'] + '`' in body, (name, param['name'])
    print(f'PASS: player guide covers all {len(guide_by_type)} commands and their constructor parameters')
    checked_links = 0
    json_blocks = 0
    for file in (p for p in artifacts if p.suffix == '.md'):
        text = file.read_text()
        for block in re.findall(r'^```json\s*\n(.*?)^```', text, re.M | re.S):
            json.loads(block)
            json_blocks += 1
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                continue
            path, _, anchor = target.partition('#')
            dest = file.parent / unquote(path) if path else file
            assert dest.exists(), (str(file), target)
            if anchor and dest.suffix == '.md':
                headings = re.findall(r'^#+ (.+)$', dest.read_text(), re.M)
                slugs = {re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings}
                assert anchor in slugs, (str(file), target)
            checked_links += 1
    assert not any(p.suffix.lower() in ('.png', '.jpg', '.jpeg', '.pem', '.env') for p in artifacts)
    print(f'PASS: {len(files)} JSON files; {len(routes)} routes; {len(commands)} command types; {constructor_count} constructors')
    print(f'PASS: {checked_links} relative links; {json_blocks} fenced JSON blocks; route parameters and constructor metadata')
    print('PASS: excluded assets')
    print('Offline documentation checks only; no POST commands or live application tests executed.')


if __name__ == '__main__':
    main()
