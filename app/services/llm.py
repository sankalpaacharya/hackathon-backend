import httpx
import asyncio
from app.config.settings import SETTINGS
from app.prompts.bank_statement import bank_statment_prompt_maker
from app.prompts.ais_prompt import ais_prompt_maker

url = f"https://api.cloudflare.com/client/v4/accounts/{SETTINGS.workerai_account_id}/ai/run/@cf/meta/llama-3.1-8b-instruct"
headers = {
    "Authorization": f"Bearer {SETTINGS.workerai_api_key}",
    "Content-Type": "application/json"
}

async def fetch_llama(prompt: str):
    payload = {
        "messages": [{"role": "user", "content": prompt}]
    }

    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(url, headers=headers, json=payload)
        return response.json()


async def get_bank_statement_summary(statements:str):
    response = await fetch_llama(bank_statment_prompt_maker(statements=statements))
    return response["result"]["response"]

async def get_ais_summary(ais_text:str):
    response = await fetch_llama(ais_prompt_maker(ais_text=ais_text))
    return response["result"]["response"]