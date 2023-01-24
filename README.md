# Pet Kare

Aplicação realizada com o intuito de auxiliar donos de PetShops para guardar os dados de animais.

## Conceitos utilizados 

Relacionamentos, Serializers, Models e View.

### Visão geral do que foi desenvolvido no projeto

1° - Diagrama de Entidade e Relacionamento

2° - Relacionamentos entre pets, grupos e características.

3° - Serializadores para validação, entrada e saída de dados para pets, grupos e características.

4° - Sobrescrita dos métodos "Create e Update" do serializer de pet.

5° - Tratamento de exceção nas rotas de criação, atualização, filtragem e deleção.

6° - Campo de leitura utilizando SerializerMethodFiled.

7° - CRUD (Create, Read, Update and Destroy) completo da rota "pet".


### Rodando o Projeto.

1. Crie seu ambiente virtual:
```bash
python -m venv venv
```

2. Ative seu venv:
```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

3. Rodando as migrações

```
python manage.py migrate
```

4. Rodando o projeto

```
python manage.py runserver
```

Obrigado ;)
