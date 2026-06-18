TOP_GENRES_QUERY = """
select
    g.nome,
    count(*) as total
from jogo_genero jg
join generos g
    on g.id = jg.genero_id
group by g.nome
order by total desc
limit 10
"""