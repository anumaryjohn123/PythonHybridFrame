from Pages.postgres import postgresql


class Test_postgres:
    def test_apiPost(self):
        cursor = postgresql(self)
        query = 'SELECT * FROM public."PermEmployee" WHERE "ID" = %s'
        params = ('2',)
        cursor.execute(query, params)

        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()
