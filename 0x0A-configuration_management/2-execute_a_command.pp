# Kill the process named "killmenow" using pkill

exec { 'killmenow_process':
  command     => '/usr/bin/pkill -f killmenow',
  refreshonly => true,
  onlyif      => '/usr/bin/pgrep -f killmenow',
}
