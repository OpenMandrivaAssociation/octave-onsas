#!/bin/sh
curl "https://github.com/ONSAS/ONSAS.m/tags" 2>/dev/null |grep "tag/v" |sed -e 's,.*tag/v,,;s,\".*,,;' |head -n1

