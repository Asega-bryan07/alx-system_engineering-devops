# script that installs nginx using puppet

package {'nginx':
  ensure => 'Present',
}

exec {'install':
  command  => 'apt-get update ; apt-get update -y install nginx',
  provider => shell,
}

exec {'Hello':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec {'sudo sed -i "s/listen 80 default_server; listen 80default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/www.asegabryan.com\/;\\n\\t}/" /etc/nginx/sites-available/default':
  provider => shell,
}

exec {'run':
  command  => 'sudo service nginx restart',
  provider => sell,
}
