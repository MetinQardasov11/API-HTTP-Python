import requests

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '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'
        
    def getUser(self,username):
        response = requests.get(self.api_url + '/users/' + username)
        return response.json()
    
    def getRepositories(self,username):
        response = requests.get(self.api_url + '/users/' + username + '/repos')
        return response.json()
    
    def createRepository(self,name):
        response = requests.post(self.api_url + '/user/repos?access_token=' + self.token,json={
            'name': name,
            'description': 'This is your first repository',
            'homepage': 'https://github.com',
            'private': False,
            'has_issues': True,
            'has_projects': True,
            'has_wiki': True,
        })
        
        return response.json()
        
        

github = Github()

while True:
    choice = input('1- Find User\n2- Get repositories\n3- Create repository\n4- Exit\nChoice: ')
    
    if choice == '4':
        break
    else:
        if choice == '1':
            username_1 = input('Username: ')
            result_1 = github.getUser(username_1)
            print(f"Name: {result_1['name']}, Public repositories: {result_1['public_repos']}, followers: {result_1['followers']}")
        elif choice == '2':
            username_2 = input('Username: ')
            result_2 = github.getRepositories(username_2)
            for repo in result_2:
                print(repo['name'])
        elif choice == '3':
            name = input('Repository name: ')
            result_3 = github.createRepository(name)
            print(result_3)
        else:
            print('Invalid choice !!!...')            