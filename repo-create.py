#!/usr/bin//env python3
import requests
import os
import keys
import subprocess
import time
API_KEY = keys.GITHUB_API_KEY


name = input('Nombre del repositorio: \n')
descripcion = input('Descripcion: \n')
privacidad = input('¿Lo queres hacer privado? (y/n): \n')
homepage = input('¿Queres agregar la homepage del proyecto? (y/n): \n')

if homepage == 'n':
  homepage = ''
else:
  homepage = input('Ingresa la URL: \n')

if privacidad == 'n':
  privacidad = False
else:
  privacidad = True


req = requests

data = {
  "name": name,
  "description": descripcion,
  "homepage": homepage,
  "private": privacidad,
  "has_issues": 'true',
  "has_projects": 'true',
  "has_wiki": 'true'
}

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/vnd.github.v3+json'}
print('Enviando petición...')
res = req.post(f'https://api.github.com/user/repos?access_token={API_KEY}', json=data, headers=headers)

json_res = res.json()
ssh_url = json_res['ssh_url']
clone_url = json_res['clone_url']
repo_url = json_res['svn_url']

selected_remote_add_method = input('SSH o HTTP? (s/h): \n')

if selected_remote_add_method == 's':
  selected_remote_add_method = ssh_url
else:
  selected_remote_add_method = clone_url
## chequear que subprocess termine para pasar al siguiente
git_remote_add = subprocess.Popen(f"git remote add origin {selected_remote_add_method}", shell=True)
while (git_remote_add.poll() == None):
  pass
git_push_master = subprocess.Popen(f"git push -u origin master", shell=True)
while(git_push_master.poll() == None):
  pass

print('\nRepositorio creado: \n',f'Visitalo en {repo_url}\n')
if input('Queres ver mas detalles de tu creacion? (y/n): \n') == 'y':
  for k, v in json_res.items():
    print(k, ':', v)