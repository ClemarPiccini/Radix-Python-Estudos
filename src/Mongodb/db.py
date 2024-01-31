import asyncio
import motor.motor_asyncio

async def main():
    # Conectar ao servidor MongoDB (por padrão, o MongoDB é executado em localhost:27017)
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/")

    # Acessar um banco de dados
    db = client["nome_do_banco"]

    # Acessar uma coleção
    col = db["nome_da_colecao"]

    # Inserir um documento
    doc = {"nome": "Exemplo", "idade": 30}
    await col.insert_one(doc)

    # Consultar documentos
    async for doc in col.find({}):
        print(doc)

if __name__ == "__main__":
    asyncio.run(main())
