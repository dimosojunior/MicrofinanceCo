from App.models import *
from django.core.mail import send_mail
from django.conf import settings

from datetime import datetime, timedelta
from django.utils.timezone import now

def run():
    try:
        today = now().date()
        wateja_list = WatejaWote.objects.all()
        deni_plus_faini = 0
        tarehe_ya_kulipa_tena_nje_ya_mkataba_wote = 0
        tarehe_ya_leo = 0
        tarehe_ya_kumaliza=0

        deni_alilomaliza_nalo = 0

        kiasi_anachokopa = 0

        riba_mpya = 0
        deni_plus_riba = 0
        rejesho_kwa_siku = 0
        


        for mteja in wateja_list:
            time_elapsed = mteja.time_left
            deni_plus_faini = mteja.JumlaYaDeni + mteja.JumlaYaFainiZote

            # if time_elapsed == 31 and mteja.Ni_Mteja_Hai and mteja.JumlaYaDeni <= 0:
            #     mteja.Ni_Mteja_Hai = False
            #     mteja.save(update_fields=['Ni_Mteja_Hai'])
                #send_email(mteja, "Ni Mteja Hai condition reached.")

            if time_elapsed == 30 and not mteja.Nje_Ya_Mkata_Leo and mteja.JumlaYaDeni > 0:
                mteja.Nje_Ya_Mkata_Leo = True
                mteja.save(update_fields=['Nje_Ya_Mkata_Leo'])
                send_email(mteja, f"Ndugu mteja {mteja.JinaKamiliLaMteja} mkataba wako unaisha leo, deni lako limebaki Tsh {deni_plus_faini}/=\n Fika ofisini kumaliza deni lako kabla mfumo haujakubadilishia mkataba mpya. \n Mawasiliano: 0621690739 / 0747462389 ")
                copy_to_nje_ya_mkataba_copies(mteja)

            if time_elapsed == 31 and mteja.Nje_Ya_Mkata_Leo:
                mteja.Nje_Ya_Mkata_Leo = False
                mteja.save(update_fields=['Nje_Ya_Mkata_Leo'])
                #send_email(mteja, "Umetoka nje ya mkataba wa siku 30.")

            #hii ni kwaajili ya kumchange mteja kuwa true kwenye mkatababa wote
            if time_elapsed == 31 and not mteja.Nje_Ya_Mkata_Wote and mteja.JumlaYaDeni > 0:
                mteja.Nje_Ya_Mkata_Wote = True
                mteja.save(update_fields=['Nje_Ya_Mkata_Wote'])
                #send_email(mteja, f"Ndugu mteja {mteja.JinaKamiliLaMteja} mkataba wako umejibadilisha leo. Deni lako jipya ni Tsh {deni_plus_faini}/=, rejesha mpaka tarehe {tarehe_ya_kulipa_tena_nje_ya_mktaba_wote}. \n Hatua zitachukuliwa ikiwa hutomaliza. \n Mawasiliano: 0621690739 / 0747462389")
            

            if time_elapsed == 40 and mteja.Nje_Ya_Mkata_Wote and mteja.JumlaYaDeni > 0:

                # Delete matching entries from MarejeshoCopies
                MarejeshoCopiesTwo.objects.filter(
                    JinaKamiliLaMteja=mteja.JinaKamiliLaMteja,
                    reg_no=mteja.reg_no
                ).delete()

                
                mteja.Nje_Ya_Mkata_Wote = False
                mteja.Nje_Ya_Mkata_Leo = False
                mteja.Ni_Mteja_Hai = True
                mteja.Amerejesha_Leo = False
                mteja.Wamemaliza_Hawajakopa_Tena = False

                deni_alilomaliza_nalo = mteja.JumlaYaDeni + mteja.JumlaYaFainiZote

                kiasi_anachokopa = int(deni_alilomaliza_nalo)

                riba_mpya = int((kiasi_anachokopa * 20) / 100)
                deni_plus_riba = kiasi_anachokopa + riba_mpya
                rejesho_kwa_siku = round((deni_plus_riba) / 30, 0)
                tarehe_ya_leo = now()
                tarehe_ya_kumaliza = tarehe_ya_leo + timedelta(days=30)

                mteja.KiasiAnachokopa = deni_plus_riba
                mteja.Riba = riba_mpya
                mteja.JumlaYaDeni = deni_plus_riba
                mteja.KiasiAlicholipa = 0
                mteja.RejeshoKwaSiku = rejesho_kwa_siku
                mteja.JumlaYaFainiZote=0




                mteja.Created = tarehe_ya_leo

                mteja.Up_To = tarehe_ya_kumaliza

                

                #calculation

                mteja.save(update_fields=[
                    'Nje_Ya_Mkata_Wote',
                    'Nje_Ya_Mkata_Leo',
                    'Ni_Mteja_Hai',
                    'Amerejesha_Leo',
                    'KiasiAnachokopa',
                    'Riba',
                    'JumlaYaDeni',
                    'KiasiAlicholipa',
                    'RejeshoKwaSiku',
                    'JumlaYaFainiZote',
                    'Wamemaliza_Hawajakopa_Tena',

                    'Created',
                    'Up_To'
                ])
                send_email(mteja, f"Ndugu mteja {mteja.JinaKamiliLaMteja} mkataba wako umejibadilisha leo. Deni lako jipya ni Tsh {deni_plus_riba}/=, rejesha mpaka tarehe {tarehe_ya_kumaliza}. \n Hatua zitachukuliwa ikiwa hutomaliza. \n Mawasiliano: 0621690739 / 0747462389")
            print(f"Executed: {mteja.JinaKamiliLaMteja}")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

def send_email(mteja, condition_message):
    subject = "Notification: Condition Met"
    message = f"Mteja: {mteja.JinaKamiliLaMteja}\nCondition: {condition_message}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [mteja.EmailYaMteja]
    send_mail(subject, message, from_email, recipient_list, fail_silently=True)

def copy_to_nje_ya_mkataba_copies(mteja):
    NjeYaMkatabaCopies.objects.create(
        JinaKamiliLaMteja=mteja.JinaKamiliLaMteja,
        JinaLaKituo=mteja.JinaLaKituo.JinaLaKituo,
        SimuYaMteja=mteja.SimuYaMteja,
        EmailYaMteja=mteja.EmailYaMteja,
        Mahali=mteja.Mahali,
        KiasiAnachokopa=mteja.KiasiAnachokopa,
        KiasiAlicholipa=mteja.KiasiAlicholipa,
        RejeshoKwaSiku=mteja.RejeshoKwaSiku,
        JumlaYaDeni=mteja.JumlaYaDeni,
        Riba=mteja.Riba,
        AmesajiliwaNa=mteja.AmesajiliwaNa,
        PichaYaMteja=mteja.PichaYaMteja,
        Ni_Mteja_Hai=mteja.Ni_Mteja_Hai,
        Updated=mteja.Updated,
        reg_no=mteja.reg_no,
        Up_To=mteja.Up_To,
    )








# def run():
#     try:
#         today = now().date()
#         wateja_list = WatejaWote.objects.all()
#         deni_plus_faini = 0
#         tarehe_ya_kulipa_tena_nje_ya_mkataba_wote = 0
#         tarehe_ya_leo = 0
#         tarehe_ya_kumaliza=0

#         deni_alilomaliza_nalo = 0

#         kiasi_anachokopa = 0

#         riba_mpya = 0
#         deni_plus_riba = 0
#         rejesho_kwa_siku = 0
        


#         for mteja in wateja_list:
#             time_elapsed = mteja.time_left
#             deni_plus_faini = mteja.JumlaYaDeni + mteja.JumlaYaFainiZote

#             # if time_elapsed == 31 and mteja.Ni_Mteja_Hai and mteja.JumlaYaDeni <= 0:
#             #     mteja.Ni_Mteja_Hai = False
#             #     mteja.save(update_fields=['Ni_Mteja_Hai'])
#                 #send_email(mteja, "Ni Mteja Hai condition reached.")

#             if time_elapsed == 30 and not mteja.Nje_Ya_Mkata_Leo and mteja.JumlaYaDeni > 0:
#                 mteja.Nje_Ya_Mkata_Leo = True
#                 mteja.save(update_fields=['Nje_Ya_Mkata_Leo'])
#                 send_email(mteja, f"Ndugu mteja {mteja.JinaKamiliLaMteja} mkataba wako unaisha leo, deni lako limebaki Tsh {deni_plus_faini}/=\n Fika ofisini kumaliza deni lako kabla mfumo haujakubadilishia mkataba mpya. \n Mawasiliano: 0621690739 / 0747462389 ")
#                 copy_to_nje_ya_mkataba_copies(mteja)

#             if time_elapsed == 31 and mteja.Nje_Ya_Mkata_Leo:
#                 mteja.Nje_Ya_Mkata_Leo = False
#                 mteja.save(update_fields=['Nje_Ya_Mkata_Leo'])
#                 #send_email(mteja, "Umetoka nje ya mkataba wa siku 30.")

#             #hii ni kwaajili ya kumchange mteja kuwa true kwenye mkatababa wote
#             if time_elapsed == 31 and not mteja.Nje_Ya_Mkata_Wote and mteja.JumlaYaDeni > 0:
#                 mteja.Nje_Ya_Mkata_Wote = True
#                 mteja.save(update_fields=['Nje_Ya_Mkata_Wote'])
#                 #send_email(mteja, f"Ndugu mteja {mteja.JinaKamiliLaMteja} mkataba wako umejibadilisha leo. Deni lako jipya ni Tsh {deni_plus_faini}/=, rejesha mpaka tarehe {tarehe_ya_kulipa_tena_nje_ya_mktaba_wote}. \n Hatua zitachukuliwa ikiwa hutomaliza. \n Mawasiliano: 0621690739 / 0747462389")
            

#             if time_elapsed == 2 and mteja.Nje_Ya_Mkata_Wote and mteja.JumlaYaDeni > 0:

#                 # Delete matching entries from MarejeshoCopies
#                 MarejeshoCopiesTwo.objects.filter(
#                     JinaKamiliLaMteja=mteja.JinaKamiliLaMteja,
#                     reg_no=mteja.reg_no
#                 ).delete()

                
#                 mteja.Nje_Ya_Mkata_Wote = False
#                 mteja.Nje_Ya_Mkata_Leo = False
#                 mteja.Ni_Mteja_Hai = True
#                 mteja.Amerejesha_Leo = False
#                 mteja.Wamemaliza_Hawajakopa_Tena = False

#                 deni_alilomaliza_nalo = mteja.JumlaYaDeni + mteja.JumlaYaFainiZote

#                 kiasi_anachokopa = int(deni_alilomaliza_nalo)

#                 riba_mpya = int((kiasi_anachokopa * 20) / 100)
#                 deni_plus_riba = kiasi_anachokopa + riba_mpya
#                 rejesho_kwa_siku = round((deni_plus_riba) / 30, 0)
#                 tarehe_ya_leo = now()
#                 tarehe_ya_kumaliza = tarehe_ya_leo + timedelta(days=30)

#                 mteja.KiasiAnachokopa = deni_plus_riba
#                 mteja.Riba = riba_mpya
#                 mteja.JumlaYaDeni = deni_plus_riba
#                 mteja.KiasiAlicholipa = 0
#                 mteja.RejeshoKwaSiku = rejesho_kwa_siku
#                 mteja.JumlaYaFainiZote=0




#                 mteja.Created = tarehe_ya_leo

#                 mteja.Up_To = tarehe_ya_kumaliza

                

#                 #calculation

#                 mteja.save(update_fields=[
#                     'Nje_Ya_Mkata_Wote',
#                     'Nje_Ya_Mkata_Leo',
#                     'Ni_Mteja_Hai',
#                     'Amerejesha_Leo',
#                     'KiasiAnachokopa',
#                     'Riba',
#                     'JumlaYaDeni',
#                     'KiasiAlicholipa',
#                     'RejeshoKwaSiku',
#                     'JumlaYaFainiZote',
#                     'Wamemaliza_Hawajakopa_Tena',

#                     'Created',
#                     'Up_To'
#                 ])
#                 send_email(mteja, f"Ndugu mteja {mteja.JinaKamiliLaMteja} mkataba wako umejibadilisha leo. Deni lako jipya ni Tsh {deni_plus_riba}/=, rejesha mpaka tarehe {tarehe_ya_kumaliza}. \n Hatua zitachukuliwa ikiwa hutomaliza. \n Mawasiliano: 0621690739 / 0747462389")
#             print(f"Executed: {mteja.JinaKamiliLaMteja}")

#     except Exception as e:
#         print(f"Error occurred: {str(e)}")

# def send_email(mteja, condition_message):
#     subject = "Notification: Condition Met"
#     message = f"Mteja: {mteja.JinaKamiliLaMteja}\nCondition: {condition_message}"
#     from_email = settings.EMAIL_HOST_USER
#     recipient_list = [mteja.EmailYaMteja]
#     send_mail(subject, message, from_email, recipient_list, fail_silently=True)

# def copy_to_nje_ya_mkataba_copies(mteja):
#     NjeYaMkatabaCopies.objects.create(
#         JinaKamiliLaMteja=mteja.JinaKamiliLaMteja,
#         JinaLaKituo=mteja.JinaLaKituo.JinaLaKituo,
#         SimuYaMteja=mteja.SimuYaMteja,
#         EmailYaMteja=mteja.EmailYaMteja,
#         Mahali=mteja.Mahali,
#         KiasiAnachokopa=mteja.KiasiAnachokopa,
#         KiasiAlicholipa=mteja.KiasiAlicholipa,
#         RejeshoKwaSiku=mteja.RejeshoKwaSiku,
#         JumlaYaDeni=mteja.JumlaYaDeni,
#         Riba=mteja.Riba,
#         AmesajiliwaNa=mteja.AmesajiliwaNa,
#         PichaYaMteja=mteja.PichaYaMteja,
#         Ni_Mteja_Hai=mteja.Ni_Mteja_Hai,
#         Updated=mteja.Updated,
#         reg_no=mteja.reg_no,
#         Up_To=mteja.Up_To,
#     )

