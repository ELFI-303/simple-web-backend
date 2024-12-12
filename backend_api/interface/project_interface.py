from database.mysql_database import MySQLDatabase

class ProjectInterface:
    def __init__(self):
        self.db = MySQLDatabase().get_db()

    def get_projects(self) -> str:
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM current_projects')
        projects = cursor.fetchall()
        return projects

    def get_project(self, id: int) -> str:
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM current_projects WHERE project_id = %s', (id,))
        project = cursor.fetchall()
        return project