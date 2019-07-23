def findDecision(obj): #obj[0]: dur, obj[1]: proto, obj[2]: service, obj[3]: state, obj[4]: spkts, obj[5]: dpkts, obj[6]: sbytes, obj[7]: dbytes, obj[8]: rate, obj[9]: sttl, obj[10]: dttl, obj[11]: sload, obj[12]: dload, obj[13]: sloss, obj[14]: dloss, obj[15]: sinpkt, obj[16]: dinpkt, obj[17]: sjit, obj[18]: djit, obj[19]: swin, obj[20]: stcpb, obj[21]: dtcpb, obj[22]: dwin, obj[23]: tcprtt, obj[24]: synack, obj[25]: ackdat, obj[26]: smean, obj[27]: dmean, obj[28]: ct_srv_src, obj[29]: ct_state_ttl, obj[30]: ct_src_dport_ltm, obj[31]: ct_dst_sport_ltm, obj[32]: ct_dst_src_ltm, obj[33]: is_ftp_login, obj[34]: ct_ftp_cmd, obj[35]: ct_srv_dst
   if obj[9]>31:
      if obj[3] == 'INT':
         if obj[1] == 'unas':
            return 'Yes'
         elif obj[1] == 'udp':
            if obj[31]<=1:
               if obj[30]<=5:
                  if obj[35]<=1:
                     if obj[11]>46222220.0:
                        if obj[26]<=96:
                           if obj[2] == '-':
                              if obj[32]<=9:
                                 if obj[0]<=1e-05:
                                    if obj[4]<=12:
                                       if obj[5]<=0:
                                          if obj[6]<=994:
                                             if obj[7]<=0:
                                                if obj[8]>90909.0902:
                                                   if obj[10]<=0:
                                                      if obj[12]<=57467.94141:
                                                         if obj[13]<=3:
                                                            if obj[14]<=3:
                                                               if obj[15]<=0.01:
                                                                  if obj[16]<=0.0:
                                                                     if obj[17]<=0.0:
                                                                        if obj[18]<=0.0:
                                                                           if obj[19]<=0:
                                                                              if obj[20]<=0:
                                                                                 if obj[21]<=0:
                                                                                    if obj[22]<=0:
                                                                                       if obj[23]<=0.0:
                                                                                          if obj[24]<=0.0:
                                                                                             if obj[25]<=0.0:
                                                                                                if obj[27]<=75:
                                                                                                   if obj[28]<=10:
                                                                                                      if obj[29]>0:
                                                                                                         if obj[33]<=0:
                                                                                                            if obj[34]<=0:
                                                                                                               return 'Yes'
                              elif obj[32]>9:
                                 return 'Yes'
                           elif obj[2] == 'snmp':
                              return 'Yes'
                        elif obj[26]>96:
                           return 'Yes'
                     elif obj[11]<=46222220.0:
                        if obj[2] == '-':
                           if obj[0]<=1e-05:
                              return 'No'
                           elif obj[0]>1e-05:
                              return 'Yes'
                        elif obj[2] == 'dns':
                           return 'No'
                  elif obj[35]>1:
                     if obj[26]<=96:
                        if obj[28]<=10:
                           if obj[0]<=1e-05:
                              if obj[11]>46222220.0:
                                 if obj[2] == '-':
                                    if obj[4]<=12:
                                       if obj[5]<=0:
                                          if obj[6]<=994:
                                             if obj[7]<=0:
                                                if obj[8]>90909.0902:
                                                   if obj[10]<=0:
                                                      if obj[12]<=57467.94141:
                                                         if obj[13]<=3:
                                                            if obj[14]<=3:
                                                               if obj[15]<=0.01:
                                                                  if obj[16]<=0.0:
                                                                     if obj[17]<=0.0:
                                                                        if obj[18]<=0.0:
                                                                           if obj[19]<=0:
                                                                              if obj[20]<=0:
                                                                                 if obj[21]<=0:
                                                                                    if obj[22]<=0:
                                                                                       if obj[23]<=0.0:
                                                                                          if obj[24]<=0.0:
                                                                                             if obj[25]<=0.0:
                                                                                                if obj[27]<=75:
                                                                                                   if obj[29]>0:
                                                                                                      if obj[32]<=9:
                                                                                                         if obj[33]<=0:
                                                                                                            if obj[34]<=0:
                                                                                                               return 'Yes'
                              elif obj[11]<=46222220.0:
                                 return 'No'
                           elif obj[0]>1e-05:
                              if obj[11]<=46222220.0:
                                 return 'Yes'
                              elif obj[11]>46222220.0:
                                 return 'No'
                        elif obj[28]>10:
                           return 'Yes'
                     elif obj[26]>96:
                        if obj[0]<=1e-05:
                           if obj[6]<=994:
                              if obj[2] == '-':
                                 if obj[4]<=12:
                                    if obj[5]<=0:
                                       if obj[7]<=0:
                                          if obj[8]>90909.0902:
                                             if obj[10]<=0:
                                                if obj[11]>46222220.0:
                                                   if obj[12]<=57467.94141:
                                                      if obj[13]<=3:
                                                         if obj[14]<=3:
                                                            if obj[15]<=0.01:
                                                               if obj[16]<=0.0:
                                                                  if obj[17]<=0.0:
                                                                     if obj[18]<=0.0:
                                                                        if obj[19]<=0:
                                                                           if obj[20]<=0:
                                                                              if obj[21]<=0:
                                                                                 if obj[22]<=0:
                                                                                    if obj[23]<=0.0:
                                                                                       if obj[24]<=0.0:
                                                                                          if obj[25]<=0.0:
                                                                                             if obj[27]<=75:
                                                                                                if obj[28]<=10:
                                                                                                   if obj[29]>0:
                                                                                                      if obj[32]<=9:
                                                                                                         if obj[33]<=0:
                                                                                                            if obj[34]<=0:
                                                                                                               return 'Yes'
                           elif obj[6]>994:
                              return 'Yes'
                        elif obj[0]>1e-05:
                           if obj[6]>994:
                              if obj[2] == '-':
                                 if obj[4]<=12:
                                    if obj[5]<=0:
                                       if obj[7]<=0:
                                          if obj[8]<=90909.0902:
                                             if obj[10]<=0:
                                                if obj[11]>46222220.0:
                                                   if obj[12]<=57467.94141:
                                                      if obj[13]<=3:
                                                         if obj[14]<=3:
                                                            if obj[15]>0.01:
                                                               if obj[16]<=0.0:
                                                                  if obj[17]<=0.0:
                                                                     if obj[18]<=0.0:
                                                                        if obj[19]<=0:
                                                                           if obj[20]<=0:
                                                                              if obj[21]<=0:
                                                                                 if obj[22]<=0:
                                                                                    if obj[23]<=0.0:
                                                                                       if obj[24]<=0.0:
                                                                                          if obj[25]<=0.0:
                                                                                             if obj[27]<=75:
                                                                                                if obj[28]<=10:
                                                                                                   if obj[29]>0:
                                                                                                      if obj[32]<=9:
                                                                                                         if obj[33]<=0:
                                                                                                            if obj[34]<=0:
                                                                                                               return 'No'
                           elif obj[6]<=994:
                              return 'No'
               elif obj[30]>5:
                  return 'No'
            elif obj[31]>1:
               return 'Yes'
         elif obj[1] == 'ospf':
            return 'Yes'
         elif obj[1] == 'rsvp':
            return 'Yes'
         elif obj[1] == 'sctp':
            return 'Yes'
         elif obj[1] == 'pipe':
            return 'Yes'
         elif obj[1] == 'netblt':
            return 'Yes'
         elif obj[1] == 'irtp':
            return 'Yes'
         elif obj[1] == 'ddp':
            return 'Yes'
         elif obj[1] == 'idpr-cmtp':
            return 'Yes'
         elif obj[1] == 'wsn':
            return 'Yes'
         elif obj[1] == 'any':
            return 'Yes'
         elif obj[1] == 'argus':
            return 'Yes'
         elif obj[1] == 'iplt':
            return 'Yes'
         elif obj[1] == 'chaos':
            return 'Yes'
         elif obj[1] == 'kryptolan':
            return 'Yes'
         elif obj[1] == 'br-sat-mon':
            return 'Yes'
         elif obj[1] == 'uti':
            return 'Yes'
         elif obj[1] == 'aes-sp3-d':
            return 'Yes'
         elif obj[1] == 'ggp':
            return 'Yes'
         elif obj[1] == 'rvd':
            return 'Yes'
         elif obj[1] == 'ipx-n-ip':
            return 'Yes'
         elif obj[1] == 'trunk-1':
            return 'Yes'
         elif obj[1] == 'stp':
            return 'Yes'
         elif obj[1] == 'pup':
            return 'Yes'
         elif obj[1] == 'merit-inp':
            return 'Yes'
         elif obj[1] == 'ippc':
            return 'Yes'
         elif obj[1] == 'gre':
            return 'Yes'
         elif obj[1] == 'idpr':
            return 'Yes'
         elif obj[1] == 'secure-vmtp':
            return 'Yes'
         elif obj[1] == 'ax.25':
            return 'Yes'
         elif obj[1] == 'sps':
            return 'Yes'
         elif obj[1] == 'pvp':
            return 'Yes'
         elif obj[1] == 'ip':
            return 'Yes'
         elif obj[1] == 'emcon':
            return 'Yes'
         elif obj[1] == 'xtp':
            return 'Yes'
         elif obj[1] == 'ipcv':
            return 'Yes'
         elif obj[1] == 'mfe-nsp':
            return 'Yes'
         elif obj[1] == 'bbn-rcc':
            return 'Yes'
         elif obj[1] == 'leaf-2':
            return 'Yes'
         elif obj[1] == 'st2':
            return 'Yes'
         elif obj[1] == 'prm':
            return 'Yes'
         elif obj[1] == 'encap':
            return 'Yes'
         elif obj[1] == 'vmtp':
            return 'Yes'
         elif obj[1] == 'sccopmce':
            return 'Yes'
         elif obj[1] == 'cbt':
            return 'Yes'
         elif obj[1] == 'leaf-1':
            return 'Yes'
         elif obj[1] == 'ddx':
            return 'Yes'
         elif obj[1] == 'tcf':
            return 'Yes'
         elif obj[1] == 'ifmp':
            return 'Yes'
         elif obj[1] == 'swipe':
            return 'Yes'
         elif obj[1] == 'mux':
            return 'Yes'
         elif obj[1] == 'mtp':
            return 'Yes'
         elif obj[1] == 'zero':
            return 'Yes'
         elif obj[1] == 'gmtp':
            return 'Yes'
         elif obj[1] == '3pc':
            return 'Yes'
         elif obj[1] == 'idrp':
            return 'Yes'
         elif obj[1] == 'bna':
            return 'Yes'
         elif obj[1] == 'hmp':
            return 'Yes'
         elif obj[1] == 'ipv6-no':
            return 'Yes'
         elif obj[1] == 'pnni':
            return 'Yes'
         elif obj[1] == 'igp':
            return 'Yes'
         elif obj[1] == 'xns-idp':
            return 'Yes'
         elif obj[1] == 'cphb':
            return 'Yes'
         elif obj[1] == 'tp++':
            return 'Yes'
         elif obj[1] == 'ipcomp':
            return 'Yes'
         elif obj[1] == 'vines':
            return 'Yes'
         elif obj[1] == 'iso-tp4':
            return 'Yes'
         elif obj[1] == 'wb-expak':
            return 'Yes'
         elif obj[1] == 'srp':
            return 'Yes'
         elif obj[1] == 'smp':
            return 'Yes'
         elif obj[1] == 'qnx':
            return 'Yes'
         elif obj[1] == 'nsfnet-igp':
            return 'Yes'
         elif obj[1] == 'trunk-2':
            return 'Yes'
         elif obj[1] == 'ib':
            return 'Yes'
         elif obj[1] == 'ttp':
            return 'Yes'
         elif obj[1] == 'sat-mon':
            return 'Yes'
         elif obj[1] == 'ipnip':
            return 'Yes'
         elif obj[1] == 'tlsp':
            return 'Yes'
         elif obj[1] == 'isis':
            return 'Yes'
         elif obj[1] == 'etherip':
            return 'Yes'
         elif obj[1] == 'dgp':
            return 'Yes'
         elif obj[1] == 'pgm':
            return 'Yes'
         elif obj[1] == 'mobile':
            return 'Yes'
         elif obj[1] == 'vrrp':
            return 'Yes'
         elif obj[1] == 'aris':
            return 'Yes'
         elif obj[1] == 'iatp':
            return 'Yes'
         elif obj[1] == 'fire':
            return 'Yes'
         elif obj[1] == 'ipv6-frag':
            return 'Yes'
         elif obj[1] == 'compaq-peer':
            return 'Yes'
         elif obj[1] == 'sep':
            return 'Yes'
         elif obj[1] == 'xnet':
            return 'Yes'
         elif obj[1] == 'snp':
            return 'Yes'
         elif obj[1] == 'sdrp':
            return 'Yes'
         elif obj[1] == 'nvp':
            return 'Yes'
         elif obj[1] == 'ipv6-route':
            return 'Yes'
         elif obj[1] == 'ipv6':
            return 'Yes'
         elif obj[1] == 'i-nlsp':
            return 'Yes'
         elif obj[1] == 'mhrp':
            return 'Yes'
         elif obj[1] == 'pri-enc':
            return 'Yes'
         elif obj[1] == 'rdp':
            return 'Yes'
         elif obj[1] == 'sprite-rpc':
            return 'Yes'
      elif obj[3] == 'FIN':
         if obj[35]<=1:
            if obj[2] == 'http':
               if obj[27]>75:
                  return 'Yes'
               elif obj[27]<=75:
                  if obj[26]<=96:
                     if obj[32]<=9:
                        if obj[0]>1e-05:
                           if obj[1] == 'tcp':
                              if obj[4]<=12:
                                 if obj[5]>0:
                                    if obj[6]<=994:
                                       if obj[7]>0:
                                          if obj[8]<=90909.0902:
                                             if obj[10]>0:
                                                if obj[11]<=46222220.0:
                                                   if obj[12]<=57467.94141:
                                                      if obj[13]<=3:
                                                         if obj[14]<=3:
                                                            if obj[15]>0.01:
                                                               if obj[16]>0.0:
                                                                  if obj[17]>0.0:
                                                                     if obj[18]>0.0:
                                                                        if obj[19]>0:
                                                                           if obj[20]>0:
                                                                              if obj[21]>0:
                                                                                 if obj[22]>0:
                                                                                    if obj[23]>0.0:
                                                                                       if obj[24]>0.0:
                                                                                          if obj[25]>0.0:
                                                                                             if obj[28]<=10:
                                                                                                if obj[29]>0:
                                                                                                   if obj[30]<=5:
                                                                                                      if obj[31]<=1:
                                                                                                         if obj[33]<=0:
                                                                                                            if obj[34]<=0:
                                                                                                               return 'Yes'
                     elif obj[32]>9:
                        return 'Yes'
                  elif obj[26]>96:
                     return 'Yes'
            elif obj[2] == '-':
               if obj[27]<=75:
                  if obj[4]<=12:
                     if obj[6]<=994:
                        if obj[0]>1e-05:
                           if obj[1] == 'tcp':
                              if obj[5]>0:
                                 if obj[7]>0:
                                    if obj[8]<=90909.0902:
                                       if obj[10]>0:
                                          if obj[11]<=46222220.0:
                                             if obj[12]<=57467.94141:
                                                if obj[13]<=3:
                                                   if obj[14]<=3:
                                                      if obj[15]>0.01:
                                                         if obj[16]>0.0:
                                                            if obj[17]>0.0:
                                                               if obj[18]>0.0:
                                                                  if obj[19]>0:
                                                                     if obj[20]>0:
                                                                        if obj[21]>0:
                                                                           if obj[22]>0:
                                                                              if obj[23]>0.0:
                                                                                 if obj[24]>0.0:
                                                                                    if obj[25]>0.0:
                                                                                       if obj[26]<=96:
                                                                                          if obj[28]<=10:
                                                                                             if obj[29]>0:
                                                                                                if obj[30]<=5:
                                                                                                   if obj[31]<=1:
                                                                                                      if obj[32]<=9:
                                                                                                         if obj[33]<=0:
                                                                                                            if obj[34]<=0:
                                                                                                               return 'Yes'
                     elif obj[6]>994:
                        return 'Yes'
                  elif obj[4]>12:
                     if obj[6]>994:
                        if obj[0]>1e-05:
                           if obj[1] == 'tcp':
                              if obj[5]>0:
                                 if obj[7]>0:
                                    if obj[8]<=90909.0902:
                                       if obj[10]>0:
                                          if obj[11]<=46222220.0:
                                             if obj[12]<=57467.94141:
                                                if obj[13]>3:
                                                   if obj[14]<=3:
                                                      if obj[15]>0.01:
                                                         if obj[16]>0.0:
                                                            if obj[17]>0.0:
                                                               if obj[18]>0.0:
                                                                  if obj[19]>0:
                                                                     if obj[20]>0:
                                                                        if obj[21]>0:
                                                                           if obj[22]>0:
                                                                              if obj[23]>0.0:
                                                                                 if obj[24]>0.0:
                                                                                    if obj[25]>0.0:
                                                                                       if obj[26]>96:
                                                                                          if obj[28]<=10:
                                                                                             if obj[29]>0:
                                                                                                if obj[30]<=5:
                                                                                                   if obj[31]<=1:
                                                                                                      if obj[32]<=9:
                                                                                                         if obj[33]<=0:
                                                                                                            if obj[34]<=0:
                                                                                                               return 'Yes'
                     elif obj[6]<=994:
                        return 'Yes'
               elif obj[27]>75:
                  return 'Yes'
            elif obj[2] == 'smtp':
               if obj[27]>75:
                  if obj[4]>12:
                     if obj[17]>0.0:
                        if obj[32]<=9:
                           if obj[0]>1e-05:
                              if obj[1] == 'tcp':
                                 if obj[5]>0:
                                    if obj[6]>994:
                                       if obj[7]>0:
                                          if obj[8]<=90909.0902:
                                             if obj[10]>0:
                                                if obj[11]<=46222220.0:
                                                   if obj[12]<=57467.94141:
                                                      if obj[13]>3:
                                                         if obj[14]>3:
                                                            if obj[15]>0.01:
                                                               if obj[16]>0.0:
                                                                  if obj[18]>0.0:
                                                                     if obj[19]>0:
                                                                        if obj[20]>0:
                                                                           if obj[21]>0:
                                                                              if obj[22]>0:
                                                                                 if obj[23]>0.0:
                                                                                    if obj[24]>0.0:
                                                                                       if obj[25]>0.0:
                                                                                          if obj[26]>96:
                                                                                             if obj[28]<=10:
                                                                                                if obj[29]>0:
                                                                                                   if obj[30]<=5:
                                                                                                      if obj[31]<=1:
                                                                                                         if obj[33]<=0:
                                                                                                            if obj[34]<=0:
                                                                                                               return 'Yes'
                        elif obj[32]>9:
                           return 'Yes'
                     elif obj[17]<=0.0:
                        return 'Yes'
                  elif obj[4]<=12:
                     return 'Yes'
               elif obj[27]<=75:
                  return 'Yes'
            elif obj[2] == 'ftp-data':
               return 'Yes'
            elif obj[2] == 'ftp':
               return 'Yes'
            elif obj[2] == 'pop3':
               return 'Yes'
            elif obj[2] == 'irc':
               return 'Yes'
         elif obj[35]>1:
            if obj[6]<=994:
               if obj[13]<=3:
                  if obj[2] == '-':
                     if obj[12]<=57467.94141:
                        if obj[27]<=75:
                           if obj[32]<=9:
                              if obj[28]<=10:
                                 if obj[31]<=1:
                                    if obj[0]>1e-05:
                                       if obj[1] == 'tcp':
                                          if obj[4]<=12:
                                             if obj[5]>0:
                                                if obj[7]>0:
                                                   if obj[8]<=90909.0902:
                                                      if obj[10]>0:
                                                         if obj[11]<=46222220.0:
                                                            if obj[14]<=3:
                                                               if obj[15]>0.01:
                                                                  if obj[16]>0.0:
                                                                     if obj[17]>0.0:
                                                                        if obj[18]>0.0:
                                                                           if obj[19]>0:
                                                                              if obj[20]>0:
                                                                                 if obj[21]>0:
                                                                                    if obj[22]>0:
                                                                                       if obj[23]>0.0:
                                                                                          if obj[24]>0.0:
                                                                                             if obj[25]>0.0:
                                                                                                if obj[26]<=96:
                                                                                                   if obj[29]>0:
                                                                                                      if obj[30]<=5:
                                                                                                         if obj[33]<=0:
                                                                                                            if obj[34]<=0:
                                                                                                               return 'No'
                                 elif obj[31]>1:
                                    if obj[0]>1e-05:
                                       if obj[1] == 'tcp':
                                          if obj[4]<=12:
                                             if obj[5]>0:
                                                if obj[7]>0:
                                                   if obj[8]<=90909.0902:
                                                      if obj[10]>0:
                                                         if obj[11]<=46222220.0:
                                                            if obj[14]<=3:
                                                               if obj[15]>0.01:
                                                                  if obj[16]>0.0:
                                                                     if obj[17]>0.0:
                                                                        if obj[18]>0.0:
                                                                           if obj[19]>0:
                                                                              if obj[20]>0:
                                                                                 if obj[21]>0:
                                                                                    if obj[22]>0:
                                                                                       if obj[23]>0.0:
                                                                                          if obj[24]>0.0:
                                                                                             if obj[25]>0.0:
                                                                                                if obj[26]<=96:
                                                                                                   if obj[29]>0:
                                                                                                      if obj[30]<=5:
                                                                                                         if obj[33]<=0:
                                                                                                            if obj[34]<=0:
                                                                                                               return 'No'
                              elif obj[28]>10:
                                 return 'Yes'
                           elif obj[32]>9:
                              return 'No'
                        elif obj[27]>75:
                           return 'Yes'
                     elif obj[12]>57467.94141:
                        return 'No'
                  elif obj[2] == 'http':
                     if obj[27]>75:
                        if obj[12]<=57467.94141:
                           if obj[26]<=96:
                              if obj[31]<=1:
                                 if obj[0]>1e-05:
                                    if obj[1] == 'tcp':
                                       if obj[4]<=12:
                                          if obj[5]>0:
                                             if obj[7]>0:
                                                if obj[8]<=90909.0902:
                                                   if obj[10]>0:
                                                      if obj[11]<=46222220.0:
                                                         if obj[14]<=3:
                                                            if obj[15]>0.01:
                                                               if obj[16]>0.0:
                                                                  if obj[17]>0.0:
                                                                     if obj[18]>0.0:
                                                                        if obj[19]>0:
                                                                           if obj[20]>0:
                                                                              if obj[21]>0:
                                                                                 if obj[22]>0:
                                                                                    if obj[23]>0.0:
                                                                                       if obj[24]>0.0:
                                                                                          if obj[25]>0.0:
                                                                                             if obj[28]<=10:
                                                                                                if obj[29]>0:
                                                                                                   if obj[30]<=5:
                                                                                                      if obj[32]<=9:
                                                                                                         if obj[33]<=0:
                                                                                                            if obj[34]<=0:
                                                                                                               return 'No'
                              elif obj[31]>1:
                                 return 'No'
                           elif obj[26]>96:
                              return 'Yes'
                        elif obj[12]>57467.94141:
                           return 'Yes'
                     elif obj[27]<=75:
                        return 'Yes'
                  elif obj[2] == 'ftp':
                     return 'Yes'
               elif obj[13]>3:
                  return 'Yes'
            elif obj[6]>994:
               if obj[28]<=10:
                  if obj[13]<=3:
                     if obj[31]<=1:
                        if obj[4]<=12:
                           if obj[2] == '-':
                              if obj[26]>96:
                                 if obj[27]<=75:
                                    if obj[32]<=9:
                                       if obj[0]>1e-05:
                                          if obj[1] == 'tcp':
                                             if obj[5]>0:
                                                if obj[7]>0:
                                                   if obj[8]<=90909.0902:
                                                      if obj[10]>0:
                                                         if obj[11]<=46222220.0:
                                                            if obj[12]<=57467.94141:
                                                               if obj[14]<=3:
                                                                  if obj[15]>0.01:
                                                                     if obj[16]>0.0:
                                                                        if obj[17]>0.0:
                                                                           if obj[18]>0.0:
                                                                              if obj[19]>0:
                                                                                 if obj[20]>0:
                                                                                    if obj[21]>0:
                                                                                       if obj[22]>0:
                                                                                          if obj[23]>0.0:
                                                                                             if obj[24]>0.0:
                                                                                                if obj[25]>0.0:
                                                                                                   if obj[29]>0:
                                                                                                      if obj[30]<=5:
                                                                                                         if obj[33]<=0:
                                                                                                            if obj[34]<=0:
                                                                                                               return 'Yes'
                                    elif obj[32]>9:
                                       return 'Yes'
                                 elif obj[27]>75:
                                    return 'Yes'
                              elif obj[26]<=96:
                                 if obj[0]>1e-05:
                                    if obj[1] == 'tcp':
                                       if obj[5]>0:
                                          if obj[7]>0:
                                             if obj[8]<=90909.0902:
                                                if obj[10]>0:
                                                   if obj[11]<=46222220.0:
                                                      if obj[12]<=57467.94141:
                                                         if obj[14]<=3:
                                                            if obj[15]>0.01:
                                                               if obj[16]>0.0:
                                                                  if obj[17]>0.0:
                                                                     if obj[18]>0.0:
                                                                        if obj[19]>0:
                                                                           if obj[20]>0:
                                                                              if obj[21]>0:
                                                                                 if obj[22]>0:
                                                                                    if obj[23]>0.0:
                                                                                       if obj[24]>0.0:
                                                                                          if obj[25]>0.0:
                                                                                             if obj[27]>75:
                                                                                                if obj[29]>0:
                                                                                                   if obj[30]<=5:
                                                                                                      if obj[32]<=9:
                                                                                                         if obj[33]<=0:
                                                                                                            if obj[34]<=0:
                                                                                                               return 'Yes'
                           elif obj[2] == 'http':
                              if obj[27]>75:
                                 if obj[0]>1e-05:
                                    if obj[1] == 'tcp':
                                       if obj[5]>0:
                                          if obj[7]>0:
                                             if obj[8]<=90909.0902:
                                                if obj[10]>0:
                                                   if obj[11]<=46222220.0:
                                                      if obj[12]<=57467.94141:
                                                         if obj[14]<=3:
                                                            if obj[15]>0.01:
                                                               if obj[16]>0.0:
                                                                  if obj[17]>0.0:
                                                                     if obj[18]>0.0:
                                                                        if obj[19]>0:
                                                                           if obj[20]>0:
                                                                              if obj[21]>0:
                                                                                 if obj[22]>0:
                                                                                    if obj[23]>0.0:
                                                                                       if obj[24]>0.0:
                                                                                          if obj[25]>0.0:
                                                                                             if obj[26]>96:
                                                                                                if obj[29]>0:
                                                                                                   if obj[30]<=5:
                                                                                                      if obj[32]<=9:
                                                                                                         if obj[33]<=0:
                                                                                                            if obj[34]<=0:
                                                                                                               return 'Yes'
                              elif obj[27]<=75:
                                 return 'Yes'
                           elif obj[2] == 'ftp':
                              return 'Yes'
                        elif obj[4]>12:
                           return 'Yes'
                     elif obj[31]>1:
                        return 'Yes'
                  elif obj[13]>3:
                     if obj[31]<=1:
                        if obj[2] == '-':
                           if obj[26]>96:
                              if obj[12]<=57467.94141:
                                 if obj[27]<=75:
                                    if obj[14]<=3:
                                       if obj[0]>1e-05:
                                          if obj[1] == 'tcp':
                                             if obj[4]>12:
                                                if obj[5]>0:
                                                   if obj[7]>0:
                                                      if obj[8]<=90909.0902:
                                                         if obj[10]>0:
                                                            if obj[11]<=46222220.0:
                                                               if obj[15]>0.01:
                                                                  if obj[16]>0.0:
                                                                     if obj[17]>0.0:
                                                                        if obj[18]>0.0:
                                                                           if obj[19]>0:
                                                                              if obj[20]>0:
                                                                                 if obj[21]>0:
                                                                                    if obj[22]>0:
                                                                                       if obj[23]>0.0:
                                                                                          if obj[24]>0.0:
                                                                                             if obj[25]>0.0:
                                                                                                if obj[29]>0:
                                                                                                   if obj[30]<=5:
                                                                                                      if obj[32]<=9:
                                                                                                         if obj[33]<=0:
                                                                                                            if obj[34]<=0:
                                                                                                               return 'Yes'
                                    elif obj[14]>3:
                                       return 'Yes'
                                 elif obj[27]>75:
                                    return 'Yes'
                              elif obj[12]>57467.94141:
                                 return 'No'
                           elif obj[26]<=96:
                              return 'Yes'
                        elif obj[2] == 'http':
                           return 'Yes'
                     elif obj[31]>1:
                        return 'Yes'
               elif obj[28]>10:
                  return 'No'
      elif obj[3] == 'CON':
         if obj[29]>0:
            if obj[2] == '-':
               return 'No'
            elif obj[2] == 'smtp':
               return 'Yes'
         elif obj[29]<=0:
            return 'Yes'
      elif obj[3] == 'RST':
         return 'No'
      elif obj[3] == 'REQ':
         return 'Yes'
      elif obj[3] == 'ECO':
         return 'No'
   elif obj[9]<=31:
      return 'No'
