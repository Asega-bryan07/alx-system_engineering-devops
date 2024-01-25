# enable a user at Holberton to login and open files without any error

# increase the limit in the hardfile for Holberton user
exec { 'increase-hard-file-limit-for-holberton-user':
  command => "sed -i '^holberton hard/s/4/50000/' /etc/security/limits.conf",
  path    => 'user/local/bin/:/bin/'
}

#increase soft file limit for Holberton user
exec { 'increase-soft-file-limit-for-holberton-user':
  command => "sed -i '^holberton hard/s/5/50000/' /etc/security/limits.conf",
  path    => 'user/local/bin/:/bin/'}
