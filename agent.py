import os, sys
from dotenv import load_dotenv
from openai import OpenAI

def main():
load_dotenv()
api = os.getenv("OPENAI_API_KEY")
if not api:
raise SystemExit("Set OPENAI_API_KEY in .env")
model = os.getenv("MODEL","gpt-4o-mini")
prompt = " ".join(sys.argv[1:]) or "Say hello"
client = OpenAI(api_key=api)
resp = client.chat.completions.create(
model=model,
messages=[{"role":"user","content":prompt}],
temperature=0.2,
)
print(resp.choices[0].message.content.strip())

if name == "main":
main()
