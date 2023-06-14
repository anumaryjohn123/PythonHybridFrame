from Pages.postgres import postgresql
import allure
import pytest


@pytest.mark.description("Validate Postgres Results")
@allure.title('Successful Data extraction from DB')
class Test_postgres:
    def test_PostgreSQLValidation(self):
        cursor = postgresql(self)
        query = 'SELECT * FROM public."PermEmployee" WHERE "ID" = %s'
        params = ('2',)
        cursor.execute(query, params)

        rows = cursor.fetchall()

        for row in rows:
            print(row)
        print("************** Successfully Able to retrieve data from PostgreSQL******** \n")
        cursor.close()
