# Kill the process named "killmenow" using pkill

exec { 'killmenow_process':
  command     => 'pkill -f killmenow',
  refreshonly => true,
  onlyif      => 'pgrep -f killmenow',
}
