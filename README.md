# exim-transient

Create temporary email aliases with included expiry date by adding prefixis like 20201231_ to any email address. The afore mentioned prefix will result in emails being accepted until January 1st 2021.


## Exim integration

```
      transient_email:
        debug_print                     = "R: transient_email for $local_part@$domain"
        driver                          = queryprogram
        domains                         = +main_domains
        command                         = /path/to/exim-transient.py $local_part@$domain
        command_user                    = ${config.services.exim.user}
        condition                       = ''${if match{$local_part}{^\\d\{8\}_}}
        timeout                         = 2s
```

