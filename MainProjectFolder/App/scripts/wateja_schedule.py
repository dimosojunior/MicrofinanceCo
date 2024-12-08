from App.models import WatejaWote2, NjeYaMkatabaCopies
from django.core.mail import send_mail
from django.conf import settings
from django.utils.timezone import now

def run():
    try:
        today = now().date()
        wateja_list = WatejaWote2.objects.all()

        for mteja in wateja_list:
            time_elapsed = mteja.time_left

            if time_elapsed == 5 and mteja.Ni_Mteja_Hai:
                mteja.Ni_Mteja_Hai = False
                mteja.save(update_fields=['Ni_Mteja_Hai'])
                send_email(mteja, "Ni Mteja Hai condition reached.")

            if time_elapsed == 4 and not mteja.Nje_Ya_Mkata_Leo:
                mteja.Nje_Ya_Mkata_Leo = True
                mteja.save(update_fields=['Nje_Ya_Mkata_Leo'])
                send_email(mteja, "Nje Ya Mkata Leo condition reached.")
                copy_to_nje_ya_mkataba_copies(mteja)

            if time_elapsed == 5 and mteja.Nje_Ya_Mkata_Leo:
                mteja.Nje_Ya_Mkata_Leo = False
                mteja.save(update_fields=['Nje_Ya_Mkata_Leo'])
                send_email(mteja, "Umetoka nje ya mkataba wa siku 30.")

            if time_elapsed == 5 and not mteja.Nje_Ya_Mkata_Wote:
                mteja.Nje_Ya_Mkata_Wote = True
                mteja.save(update_fields=['Nje_Ya_Mkata_Wote'])
                send_email(mteja, "Nje Ya Mkata Wote condition reached.")
            
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
