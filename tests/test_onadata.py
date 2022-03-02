import pytest, pandas
from onadata.onadata import list_sets, caviar_end, caviar_middle, caviar_start, chinook_customers, chinook_employees, chinook_invoices, chinook_items, dolphins, email_edgelist, email_vertices, eu_referendum, friends_tv_edgelist, g14_edgelist, karate, koenigsberg, lesmis, londontube_edgelist, londontube_vertices, madmen_edges, madmen_vertices, netscience, ontariopol_vertices, ontariopol_edgelist, park_reviews, pizza, s50_edges, s50_vertices, schoolfriends_edgelist, schoolfriends_vertices, wikivote, workfrance_vertices, workfrance_edgelist

def test_shape_of_output():
    assert len(list_sets()) == 32
    assert caviar_end().shape[1] == 3
    assert caviar_middle().shape[1] == 3
    assert caviar_start().shape[1] == 3
    assert chinook_customers().shape[1] == 4
    assert chinook_employees().shape[1] == 4
    assert chinook_invoices().shape[1] == 2
    assert chinook_items().shape[1] == 2
    assert dolphins().shape[1] == 2
    assert email_edgelist().shape[1] == 2
    assert email_vertices().shape[1] == 2
    assert eu_referendum().shape[1] == 4
    assert friends_tv_edgelist().shape[1] == 3
    assert g14_edgelist().shape[1] == 3
    assert karate().shape[1] == 2
    assert koenigsberg().shape[1] == 2
    assert lesmis().shape[1] == 3
    assert londontube_edgelist().shape[1] == 4
    assert londontube_vertices().shape[1] == 4
    assert madmen_edges().shape[1] == 3
    assert madmen_vertices().shape[1] == 3
    assert netscience().shape[1] == 3
    assert ontariopol_edgelist().shape[1] == 3
    assert ontariopol_vertices().shape[1] == 4
    assert park_reviews().shape[1] == 4
    assert pizza().shape[1] == 5
    assert s50_edges().shape[1] == 2
    assert s50_vertices().shape[1] == 5
    assert schoolfriends_edgelist().shape[1] == 3
    assert schoolfriends_vertices().shape[1] == 3
    assert wikivote().shape[1] == 2
    assert workfrance_edgelist().shape[1] == 3
    assert workfrance_vertices().shape[1] == 2
    
