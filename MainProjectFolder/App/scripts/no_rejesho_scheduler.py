from App.models import *
from django.utils.timezone import now
from datetime import timedelta

def run():
    today = now().date()
    mteja_hai = WatejaWote2.objects.filter(Ni_Mteja_Hai=True, Amerejesha_Leo=False)

    for mteja in mteja_hai:
        if not MarejeshoCopies.objects.filter(
            JinaKamiliLaMteja=mteja.JinaKamiliLaMteja, Created__date=today
        ).exists():
            mteja.JumlaYaFainiZote = (mteja.JumlaYaFainiZote or 0) + 1000
            mteja.save()
            MarejeshoCopies.objects.create(
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
                Up_To=mteja.Up_To,
                reg_no=mteja.reg_no,
                FainiKwaSiku=1000
            )
            print(f"Processed: {mteja.JinaKamiliLaMteja}")
