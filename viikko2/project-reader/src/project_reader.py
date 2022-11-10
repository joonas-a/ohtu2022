import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        formatted = toml.loads(content)
        nimi = formatted['tool']['poetry']['name']
        desc = formatted['tool']['poetry']['description']
        dependencies = [x for x in formatted['tool']['poetry']['dependencies']]
        dev_dependencies = [x for x in formatted['tool']['poetry']['dev-dependencies']]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(nimi, desc, dependencies, dev_dependencies)
