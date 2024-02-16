---
title: First App With Huggingface
emoji: 🐢
colorFrom: green
colorTo: pink
sdk: streamlit
sdk_version: 1.31.0
app_file: app.py
pinned: false
license: apache-2.0
---

1. Create a HuggingFace space
2. Clone that space locally
3. Create an `app.py` file and an `requirements.txt` file. 
4. Write your code in the `app.py` file and the libraries you use in the `requirements.txt` file. 
5. Add, commit, push your code back to hugginface. 
6. Make money. 


## How to make this in literally 2 mins [video](https://www.youtube.com/watch?v=3bSVKNKb_PY&t=1s&ab_channel=HuggingFace) and [docs](https://huggingface.co/spaces/launch).


link to this app --> https://huggingface.co/spaces/KingZack/first-app-with-huggingface

Clone url: 
```
git clone https://huggingface.co/spaces/KingZack/first-app-with-huggingface
```

### Error when pushing? 
```bash
$ git push
Username for 'https://huggingface.co': KingZack
Password for 'https://KingZack@huggingface.co':

remote: Password authentication in git is no longer supported. You must use a user access token or an SSH key instead. See https://huggingface.co/blog/password-git-deprecation
```

### You need to add a write access token.  See how to do this [here](https://huggingface.co/blog/password-git-deprecation).



```bash
$: git remote set-url origin https://<user_name>:<token>@huggingface.co/<repo_path>
$: git pull origin
```

FOR THIS APP:
```
replace MY-SECRET-TOKEN with your write access key
git remote set-url origin https://KingZack:MY-SECRET-TOKEN@huggingface.co/spaces/KingZack/first-app-with-huggingface

git pull origin
```

THESE ARE WRONG:
```
WRONG:
git remote set-url origin https://KingZack:SECRET-TOKEN@huggingface.co/https://huggingface.co/spaces/KingZack/first-app-with-huggingface

WRONG:
git remote set-url origin https://KingZack:SECRET-TOKEN@huggingface.co/first-app-with-huggingface
```