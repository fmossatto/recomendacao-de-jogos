TOP_PLATFORMS_QUERY = """
select
    p.nome,
    count(*) as total
from jogo_plataforma jp
join plataformas p
    on p.id = jp.plataforma_id
group by p.nome
order by total desc
limit 10
"""