import json

def define_env(env):
    with open("docs/userTable.json") as f:
        data = json.load(f)
    translations = data["translations"]

    def t(key: str):
        return translations.get(key, f"[MISSING:{key}]")

    env.macro(t)