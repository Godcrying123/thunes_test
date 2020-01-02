#!/bin/bash
/usr/local/bin/python thunes/bin/thunes_manage makemigrations beneficiary quotation sender transaction
/usr/local/bin/python thunes/bin/thunes_manage migrate
/usr/local/bin/supervisord -c conf/supervisord.conf
