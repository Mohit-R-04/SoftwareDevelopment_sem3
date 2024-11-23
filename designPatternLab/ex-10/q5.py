from abc import ABC,abstractmethod

class Flat:
    def __init__(self,flatno,bhk,stat,detail):
        self.flatno=flatno
        self.bhk=bhk
        self.stat=stat
        self.detail=detail
        self.maint=0
        self.obs=[]

    def regisobs(self,obser):
        self.obs.append(obser)
    
    def remove_obs(self,obser):
        self.obs.remove(obser)

    def notifyobs(self):
        for observer in self.obs:
            observer.update(self)
    
    def updatemain(self,mainte):
        self.maint=mainte
        print("UPDATED new maintenance is:",self.maint)
        self.notifyobs()
    
    def occupy(self,det):
        self.stat="occupied"
        self.detail=det
        print(f"{self.flatno} is occupied by {self.detail}")
        self.notifyobs()

    def vacate(self):
        self.state="unoccupied"
        self.detail=None
        print(f"{self.flatno} is now vacant")
        self.notifyobs()

class observer( ABC):
    @abstractmethod
    def update(self,flat):
        pass

class admin(observer):
    def update(self,flat):
        print(f"[FOR ADMIN] Update for flat {flat.flatno}:")
        if flat.stat=="occupied":
            print("occupied by:",flat.detail)
        else:
            print("unoccupied flat")
        print(f"Maintenance Status: {'Paid' if flat.maint else 'Pending'}")

class client(observer):
    def update(self,flat):
        print(f"[FOR CLIENT] Update for flat {flat.flatno}:")
        if flat.stat=="occupied":
            print("occupied by:",flat.detail)
        else:
            print("unoccupied flat")

flat101=Flat(flatno=101,bhk=2,stat="unoccupied",detail=None)
admin_obs=admin()
client_obs=client()
flat101.regisobs(admin_obs)
flat101.regisobs(client_obs)
flat101.occupy("Joe Marsh")
print()
flat101.updatemain(1000)
print()
flat101.vacate()


