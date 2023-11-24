# Using Puppet, create a manifest that kills a process named killmenow.
# Requirements:
# Must use the exec Puppet resource
# Must use pkill
# Example:
# Terminal #0 - starting my process
exec { 'kill':
command => 'pkill -f killmenow',
path => ['/usr/bin', '/usr/bin']
}
