# a puppet script to replace a line in a certain file on a server

$edited_file = 'var/www/html/wp-settings.php'

#to replace the line with `phpp` with the actual `php`

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${edited_file}",
  path    => ['/bin','/usr/bin']
}
