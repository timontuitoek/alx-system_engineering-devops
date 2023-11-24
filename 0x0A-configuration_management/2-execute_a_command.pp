# Kill the process named "killmenow" using pkill

exec { 'kill':
  command     => 'pkill killmenow',
  path    => '/usr/local/bin/:/bin/'
}
