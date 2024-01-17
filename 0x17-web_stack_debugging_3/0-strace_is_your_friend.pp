# a puppet script to replace a line in a certain file on a server

$file_to_edit = '/var/www/html/wp-settings.php'

#replace line having "phpp" with "php"

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
}
