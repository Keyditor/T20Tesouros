import git

def Update():
    git.Repo.clone_from("https://github.com/Keyditor/T20Tesouros.git","gitclone")

Update()
