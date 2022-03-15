def secrets():
    return {"host": "pg.pg4e.com",
            "port": 5432,
            "database": "pg4e_11a47e7d53",
            "user": "pg4e_11a47e7d53",
            "pass": "pg4e_p_cffa18ffa866593"}

def elastic() :
    return {"host": "www.pg4e.com",
            "prefix" : "elasticsearch",
            "port": 443,
            "scheme": "https",
            "user": "pg4e_bf813e65a9",
            "pass": "2111_0875baef"}

def readonly():
    return {"host": "pg.pg4e.com",
            "port": 5432,
            "database": "readonly",
            "user": "readonly",
            "pass": "readonly_password"}