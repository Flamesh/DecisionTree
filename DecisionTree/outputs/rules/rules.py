def findDecision(obj): #obj[0]: dur, obj[1]: proto, obj[2]: service, obj[3]: state, obj[4]: spkts, obj[5]: dpkts, obj[6]: sbytes, obj[7]: dbytes, obj[8]: rate, obj[9]: sttl, obj[10]: dttl, obj[11]: sload, obj[12]: dload, obj[13]: sloss, obj[14]: dloss, obj[15]: sinpkt, obj[16]: dinpkt, obj[17]: sjit, obj[18]: djit, obj[19]: swin, obj[20]: stcpb, obj[21]: dtcpb, obj[22]: dwin, obj[23]: tcprtt, obj[24]: synack, obj[25]: ackdat, obj[26]: smean, obj[27]: dmean, obj[28]: ct_srv_src, obj[29]: ct_state_ttl, obj[30]: ct_src_dport_ltm, obj[31]: ct_dst_sport_ltm, obj[32]: ct_dst_src_ltm, obj[33]: is_ftp_login, obj[34]: ct_ftp_cmd, obj[35]: ct_srv_dst
   if obj[1] == 'tcp':
      if obj[2] == '-':
         if obj[16]>53.433144999999996:
            if obj[9]>62:
               if obj[21]>7465531:
                  if obj[24]>0.026299:
                     return 'No'
                  elif obj[24]<=0.026299:
                     return 'Yes'
               elif obj[21]<=7465531:
                  return 'Yes'
            elif obj[9]<=62:
               return 'Yes'
         elif obj[16]<=53.433144999999996:
            if obj[3] == 'FIN':
               return 'Yes'
            elif obj[3] == 'REQ':
               return 'No'
      elif obj[2] == 'http':
         return 'Yes'
      elif obj[2] == 'ftp-data':
         return 'Yes'
      elif obj[2] == 'ftp':
         if obj[9]<=62:
            return 'Yes'
         elif obj[9]>62:
            return 'No'
      elif obj[2] == 'smtp':
         return 'Yes'
      elif obj[2] == 'pop3':
         return 'Yes'
   elif obj[1] == 'unas':
      return 'Yes'
   elif obj[1] == 'udp':
      if obj[26]<=76:
         return 'No'
      elif obj[26]>76:
         return 'Yes'
   elif obj[1] == 'arp':
      return 'No'
   elif obj[1] == 'crudp':
      return 'Yes'
   elif obj[1] == 'sccopmce':
      return 'Yes'
   elif obj[1] == 'smp':
      return 'Yes'
   elif obj[1] == 'ospf':
      return 'Yes'
   elif obj[1] == 'isis':
      return 'Yes'
   elif obj[1] == 'crtp':
      return 'Yes'
   elif obj[1] == 'sps':
      return 'Yes'
   elif obj[1] == 'sctp':
      return 'Yes'
   elif obj[1] == 'iplt':
      return 'Yes'
   elif obj[1] == 'fire':
      return 'Yes'
   elif obj[1] == 'ptp':
      return 'Yes'
   elif obj[1] == 'pipe':
      return 'Yes'
   elif obj[1] == 'fc':
      return 'Yes'
