TOP_THEMES_QUERY = """
select
    t.nome,
    count(*) as total
from jogo_tema jt
join temas t
    on t.id = jt.tema_id
group by t.nome
order by total desc
limit 10
"""