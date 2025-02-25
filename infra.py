import pulumi
import pulumi_docker as docker

config = pulumi.Config()
backend_port = config.get_int("backend_port") or 8000
frontend_port = config.get_int("frontend_port") or 8042

# Cria uma rede Docker para comunicação entre containers
network = docker.Network("escola-network")

# Função para criar containers dinamicamente
def criar_container(nome, imagem, porta_interna, porta_externa):
    return docker.Container(
        nome,
        image=imagem,
        ports=[{"internal": porta_interna, "external": porta_externa}],
        networks_advanced=[{"name": network.name}]
    )

# Criando containers
backend = criar_container("api-container", "gabiribeiro/api-escola:latest", 8000, backend_port)
frontend = criar_container("web-container", "gabiribeiro/web-escola:latest", 80, frontend_port)