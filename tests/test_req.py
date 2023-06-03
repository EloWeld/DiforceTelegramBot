from handlers.req import search_objects


def test_search_req():
    objects = [
        dict(
            Manufacturer="Hoco",
            ProductName="Чехол Hoco для iPhone XS",
            ProductArt="65163528"
        )
    ]
    d = search_objects(objects,
                       "Hoco iPhone XS Чехлы")
    assert d == objects
    
def test_search_req_fail():
    objects = [
        dict(
            Manufacturer="Hoco",
            ProductName="Чехол Hoco для iPhone XS",
            ProductArt="65163528"
        )
    ]
    d = search_objects(objects,
                       "Hoco iPhone XSS Чехландос")
    assert d == []