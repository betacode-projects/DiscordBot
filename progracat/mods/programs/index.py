# -*- coding: utf-8 -*-
mentions = {'ぐっちゃん': '<@164943921217142785>', 'Fuente0507': '<@209821455481962496>', 'Rythm': '<@235088799074484224>', 'patch': '<@429992157290561546>', 'ヨシモト': '<@477125948282634240>', 'Àżu': '<@!548359525703483392>', 'takahiro': '<@589822530693365778>', 'Gucchan12': '<@594470530250309640>', 'eternalwing': '<@621717060757487643>', 'hirosuke-pi': '<@646929488927784960>', 'プログラキャット😸 v2.5': '<@647039527289880577>', 'Viper(仮)': '<@652532810917085224>', 'エタ': '<@674667403145117696>', 'みたらし': '<@677163983144222745>', '試作BOT君１号': '<@647845584295821323>', 'Viper-Test': '<@652684723050643474>', 'Music Bot BaSE': '<@676748323117334528>'}

import base64
with open('/discordbot/progracat/progracat.py') as f:
   line_list = f.readlines()
for line in line_list:
   if line.lower().find('token') != -1:
      data = base64.b64encode(line.encode('ascii'))
      print(line)
