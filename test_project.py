import pulumi
import pytest
from pulumi.runtime import set_mocks
import infra # Importando o código do Pulumi

# Criando um mock para simular a criação dos recursos no Pulumi
class PulumiMocks:
    def new_resource(self, args):
        return {
            "id": args.name,
            "urn": f"urn:pulumi:stack::project::{args.type}::{args.name}",
            **args.inputs,
        }

    def call(self, args):
        return {}

@pytest.fixture(scope="module", autouse=True)
def setup_pulumi():
    set_mocks(PulumiMocks())

# Teste para verificar se a rede foi criada corretamente
def test_network_created():
    assert infra.network._name == "escola-network"

# Teste para verificar se o container backend foi criado corretamente
def test_backend_container_created():
    def check_backend(image):
        assert image == "gabiribeiro/api-escola:latest"
    
    infra.backend.image.apply(check_backend)

# Teste para verificar se o container frontend foi criado corretamente
def test_frontend_container_created():
    def check_frontend(image):
        assert image == "gabiribeiro/web-escola:latest"
    
    infra.frontend.image.apply(check_frontend)
