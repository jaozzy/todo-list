<strong><h1>Guia de uso (English version bellow):</h1></strong>

<strong><h2>Primeira etapa:</h2></strong>

<h3>Instale as depenências através do seguinte comando:</h3>

<pre>pip install requirements.txt</pre>

<strong><h2>Segunda etapa:</h2></strong>

<h3>Crie um banco de dados MySQL com o seguinte comando no ambiente de desenvolviemento MySQL:</h3>

<pre>
  create database todo_list
  default character set utf8
  default collate utf8_general_ci;
  
  use todo_list;
  
  create table lista (
  id int auto_increment NOT NULL,
  tarefa varchar(50),
  stts enum ('C', 'N') default 'N',
  primary key (id)
  ) default charset = utf8;
</pre>

<strong><h2>Terceira etapa:</h2></strong>

<h3>Sincronize suas informações de host do banco de dados com o arquivo main.py</h3>

<pre>
  db_connection = mysql.connector.connect(
  host='127.0.0.1',
  user='root',
  database='todo_list'
)
</pre>

<strong><h2>Quarta etapa:</h2></strong>

<h3>Escolha a linguagem do programa através do arquivo .json alterando a tag "lang". As opções são Português "pt" e Inglês "en"</h3>

<strong><h2>Quinta Etapa:</h2></strong>

<h3>Apenas adicione suas tarefas :)</h3>

<br>
<hr>
<br>

<strong><h2>Usage guide:</h2></strong>

<strong><h2>First step:</h2></strong>

<h3>Install the requiremenst with the following command:</h3>

<pre>pip install requirements.txt</pre>

<strong><h2>Second step:</h2></strong>

<h3>Create an MySQL database with the following code:</h3>

<pre>
  create database todo_list
  default character set utf8
  default collate utf8_general_ci;
  
  use todo_list;
  
  create table lista (
  id int auto_increment NOT NULL,
  tarefa varchar(50),
  stts enum ('C', 'N') default 'N',
  primary key (id)
  ) default charset = utf8;
</pre>

<strong><h2>Third Step:</h2></strong>

<h3>Sync your database host info with the python main.py script</h3>

<pre>
  db_connection = mysql.connector.connect(
  host='127.0.0.1',
  user='root',
  database='todo_list'
)
</pre>

<strong><h2>Fourth Step:</h2></strong>

<h3>Choose the code language in the .json file by changing the tag "lang". The Options are English "en" and Portuguese "pt"</h3>

<strong><h2>Fifth Step:</h2></strong>

<h3>Just add your tasks :)</h3>
