# increases the amount of service that an nginx service can gandle

# Increases the ULIMIT of the default file
exec { 'fix--for-nginx':
  # modify the ULIMIT value
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  #Specify the path for the sed command
  path    => '/usr/local/bin/:/bin/',
}

# Restart Nginx
exec { 'nginx-restart':
  # script line to restart the nginx service
  command => '/etc/init.d/nginx restart',
  # Specify the path for the init.d script
  path    => '/etc/init.d/',
  refreshonly => true,
  ignore      => [1],
  unless      => "/usr/bin/pgrep -f 'nginx: master process /usr/sbin/nginx'",
  provider    => 'shell',
  logoutput   => true,
}
