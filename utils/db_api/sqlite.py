import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            name_user varchar(255) NOT NULL,
            title str,
            name varchar(255),
            self_info varchar(255),
            education varchar(400),
            profession varchar(500),
            language varchar(255),
            desirable_job varchar(255),
            number varchar(100),
            needed varchar(255),
            company_name varchar(300),
            duties varchar(1000),
            schedule varchar(255),
            salary varchar(255),
            address varchar(200),
            contact varchar(255),
            ready_post varchar(1000),

            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int,
                 name_user: str,
                 title: str = None,
                 name: str = None,
                 self_info: str = None,
                 education: str = None,
                 profession: str = None,
                 language: str = None,
                 desirable_job: str = None,
                 number: str = None,
                 needed: str = None,
                 company_name: str = None,
                 duties: str = None,
                 schedule: str = None,
                 salary: str = None,
                 address: str = None,
                 contact: str = None,
                 ready_post: str = None
                 ):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, name_user, title, name, self_info, education, profession, language, desirable_job, number,
         needed, company_name, duties, schedule, salary, address,
        contact, ready_post) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name_user,
                                      title,
                                      name, self_info,
                                      language, profession,
                                      desirable_job, number,
                                      education, needed,
                                      company_name, duties,
                                      schedule, salary,
                                      address, contact,
                                      ready_post,
                                      ), commit=True)

    def update_ready_post(self, ready_post, id):

        sql = f"""
        UPDATE Users SET ready_post=? WHERE id=?
        """
        return self.execute(sql, parameters=(ready_post, id), commit=True)

    def update_title(self, title, id):

        sql = f"""
        UPDATE Users SET title=? WHERE id=?
        """
        return self.execute(sql, parameters=(title, id), commit=True)

    def update_contact(self, contact, id):

        sql = f"""
        UPDATE Users SET contact=? WHERE id=?
        """
        return self.execute(sql, parameters=(contact, id), commit=True)

    def update_address(self, address, id):

        sql = f"""
        UPDATE Users SET address=? WHERE id=?
        """
        return self.execute(sql, parameters=(address, id), commit=True)

    def update_salary(self, salary, id):

        sql = f"""
        UPDATE Users SET salary=? WHERE id=?
        """
        return self.execute(sql, parameters=(salary, id), commit=True)

    def update_schedule(self, schedule, id):

        sql = f"""
        UPDATE Users SET schedule=? WHERE id=?
        """
        return self.execute(sql, parameters=(schedule, id), commit=True)

    def update_duties(self, duties, id):

        sql = f"""
        UPDATE Users SET duties=? WHERE id=?
        """
        return self.execute(sql, parameters=(duties, id), commit=True)

    def update_needed(self, needed, id):

        sql = f"""
        UPDATE Users SET needed=? WHERE id=?
        """
        return self.execute(sql, parameters=(needed, id), commit=True)

    def update_company_name(self, company_name, id):

        sql = f"""
        UPDATE Users SET company_name=? WHERE id=?
        """
        return self.execute(sql, parameters=(company_name, id), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_self_info(self, self_info, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET self_info=? WHERE id=?
        """
        return self.execute(sql, parameters=(self_info, id), commit=True)

    def update_name(self, name, id):
        # SQL_EXAMPLE = "UPDATE Users SET name=name WHERE id=12345"

        sql = f"""
        UPDATE Users SET name=? WHERE id=?
        """
        return self.execute(sql, parameters=(name, id), commit=True)

    def update_education(self, education, id):
        # SQL_EXAMPLE = "UPDATE Users SET name=name WHERE id=12345"

        sql = f"""
        UPDATE Users SET education=? WHERE id=?
        """
        return self.execute(sql, parameters=(education, id), commit=True)

    def update_profession(self, profession, id):
        # SQL_EXAMPLE = "UPDATE Users SET name=name WHERE id=12345"

        sql = f"""
        UPDATE Users SET profession=? WHERE id=?
        """
        return self.execute(sql, parameters=(profession, id), commit=True)

    def update_language(self, language, id):
        # SQL_EXAMPLE = "UPDATE Users SET name=name WHERE id=12345"

        sql = f"""
        UPDATE Users SET language=? WHERE id=?
        """
        return self.execute(sql, parameters=(language, id), commit=True)

    def update_desirable_job(self, desirable_job, id):
        # SQL_EXAMPLE = "UPDATE Users SET name=name WHERE id=12345"

        sql = f"""
        UPDATE Users SET desirable_job=? WHERE id=?
        """
        return self.execute(sql, parameters=(desirable_job, id), commit=True)

    def update_number(self, number, id):
        # SQL_EXAMPLE = "UPDATE Users SET name=name WHERE id=12345"

        sql = f"""
        UPDATE Users SET number=? WHERE id=?
        """
        return self.execute(sql, parameters=(number, id), commit=True)

    def delete_users(self):
        self.execute("""DELETE FROM Users WHERE TRUE""", commit=True)

    def select_from_table(self):
        sql = """
        SELECT id FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_name(self):
        sql = """
        SELECT name_user FROM Users
        """
        return self.execute(sql, fetchall=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
