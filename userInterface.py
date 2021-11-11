import tkinter as tk
from tkinter import *
import globals as globals
import speculation

class AssetIcon:
    def __init__(self, asset, counter):
        global menuCanvas
        self.asset = asset

        if asset.name == "Bank":
            self.box = round_rectangle(100, 225+counter, 500, 275+counter)
            self.xRange = (0, 0)
            self.yRange = (0, 0)
            self.name = menuCanvas.create_text(140, 250+counter, font=("Impact", 25), text=asset.name, fill="white")
            self.marketValueTitle = menuCanvas.create_text((415, 215+counter), font=("Impact", 10),
                text="Market Value", fill="white")
            self.marketValue = menuCanvas.create_text(415, 250+counter, font=("Impact", 25),
                text="${:.2f}".format(asset.marketValue), fill="cyan3")
            self.currencyTitle = menuCanvas.create_text((275, 215+counter), font=("Impact", 10),
                text="Currency", fill="white")
            self.currency = menuCanvas.create_text(275, 250+counter, font=("Impact", 25),
                text="{0}".format(asset.currency), fill="cyan3")
            return
        if asset.name == "cadCASH":
            self.box = round_rectangle(750, 225, 1170, 275)
            self.xRange = (0, 0)
            self.yRange = (0, 0)
            self.name = menuCanvas.create_text(840, 250, font=("Impact", 25), text="TFSA CASH", fill="white")
            self.marketValueTitle = menuCanvas.create_text((1115, 215), font=("Impact", 10),
                text="Market Value", fill="white")
            self.marketValue = menuCanvas.create_text(1115, 250, font=("Impact", 25),
                text="${:.2f}".format(asset.marketValue), fill="cyan3")
            self.currencyTitle = menuCanvas.create_text((975, 215), font=("Impact", 10),
                text="Currency", fill="white")
            self.currency = menuCanvas.create_text(975, 250, font=("Impact", 25),
                text="{0}".format(asset.currency), fill="cyan3")
            return


        self.box = round_rectangle(100, 225+counter, 1170, 275+counter)
        self.xRange = (100, 1170)
        self.yRange = (225+counter, 275+counter)
        self.name = menuCanvas.create_text(175, 250+counter, font=("Impact", 25), text=asset.name, fill="white")
        
        # Adding prospector button
        prospect = menuCanvas.create_text((270, 250+counter), anchor=W, font=("Impact", 10), text="Prospect", fill="pink")
        menuCanvas.tag_bind(prospect, '<ButtonPress-1>', self.prospect)
        
        self.marketValueTitle = menuCanvas.create_text((755, 215+counter), font=("Impact", 10),
             text="Market Value", fill="white")
        self.marketValue = menuCanvas.create_text(755, 250+counter, font=("Impact", 25),
         text="${:.2f}".format(asset.marketValue), fill="cyan3")
        self.currencyTitle = menuCanvas.create_text((385, 215+counter), font=("Impact", 10),
             text="Currency", fill="white")
        self.currency = menuCanvas.create_text(385, 250+counter, font=("Impact", 25),
         text="{0}".format(asset.currency), fill="cyan3")
        if self.asset.name != "Bank":
            self.averageCostTitle = menuCanvas.create_text((555, 215+counter), font=("Impact", 10),
             text="Average Cost", fill="white")
            self.averageCost = menuCanvas.create_text(555, 250+counter, font=("Impact", 25), text="${:.2f}".format(asset.averageCost), fill="cyan3")
            self.gainLossTitle = menuCanvas.create_text((1045, 215+counter), font=("Impact", 10),
             text="Net Gain/Loss", fill="white")
            if asset.gainLossD < 0:
                self.gainLossD = menuCanvas.create_text(1045, 250+counter, font=("Impact", 25),
                 text="{0} ({1}%)".format("{0:.2f}".format(asset.gainLossD), "{0:.2f}".format(asset.gainLossP)), fill="red")
            else:
                self.gainLossD = menuCanvas.create_text(1045, 250+counter, font=("Impact", 25),
                 text="+{0} (+{1}%)".format("{0:.2f}".format(asset.gainLossD), "{0:.2f}".format(asset.gainLossP)), fill="green")

        menuCanvas.tag_bind(self.box, '<ButtonPress-1>', self.clicked)
        menuCanvas.tag_bind(self.name, '<ButtonPress-1>', self.clicked)
        menuCanvas.tag_bind(self.marketValue, '<ButtonPress-1>', self.clicked)
    
    def clicked(self, event):
        self.asset.showHistory()
    
    def prospect(self, event):
        purchaseProspector(self.asset)

class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):

        global menuCanvas

        super().__init__(container, *args, **kwargs)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=menuCanvas.yview)
        self.scrollable_frame = tk.Frame(menuCanvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: menuCanvas.configure(
                scrollregion=menuCanvas.bbox("all")
            )
        )

        menuCanvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        menuCanvas.configure(yscrollcommand=scrollbar.set)

        menuCanvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

def netWorthClicked(event):
    for asset in globals.assetListCAD:
        if asset.name == "Bank":
            asset.showHistory()

def createMenu(initialize):
    if initialize:
        global menuGui
        menuGui = tk.Tk(className="finance visualizer by Alex Dalgleish-Morel")
        
        menuGui.geometry("1280x720")
        menuGui.configure(bg='black')
        
        # Populating GUI with cyan canvas
        global menuCanvas
        scrollCoords = (0,0, (len(globals.assetListCAD)+len(globals.assetListUSD)+len(globals.prospectList))*150,
         (len(globals.assetListCAD)+len(globals.assetListUSD)+len(globals.prospectList))*150)
        menuCanvas = tk.Canvas(menuGui, bg='black', height=720, width=1250, scrollregion=scrollCoords)

        frame = ScrollableFrame(menuGui)

        title = "Financial Visualizer"
        #clickInstruct = "Click an icon to see some dope visuals of your buys/sells"
        scrollInstruct = "Click arrows to scroll"
        #frame.scrollable_frame.canvas.create_text((640, 30), anchor=W, font=("Impact", 25), text=title, fill="red")


    menuCanvas.create_text((10, 30), anchor=W, font=("Impact", 25), text=title, fill="white")
    menuCanvas.create_text((535, 100), anchor=W, font=("Impact", 15), text="Real Time Net Worth:", fill="white")
    netWorthNum = menuCanvas.create_text((450, 150), anchor=W, font=("Impact", 50), 
            text="${:.2f} CAD".format(globals.netWorth), fill="cyan")
    menuCanvas.tag_bind(netWorthNum, '<ButtonPress-1>', netWorthClicked)
    if globals.gainLossD < 0:
        menuCanvas.create_text(610, 195, font=("Impact", 15),
                    text="{0} ({1}%)".format("{0:.2f}".format(globals.gainLossD), "{0:.2f}".format(globals.gainLossP)), fill="red")
    else:
        menuCanvas.create_text(610, 195, font=("Impact", 15),
                    text="+{0} (+{1}%)".format("{0:.2f}".format(globals.gainLossD), "{0:.2f}".format(globals.gainLossP)), fill="green")
    
    menuCanvas.create_text((1100, 20), anchor=W, font=("Impact", 10), text=scrollInstruct, fill="grey")

    displayAssets()

    frame.pack()
    menuGui.mainloop()

def round_rectangle(x1, y1, x2, y2, r=25, **kwargs):    
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    global menuCanvas
    return menuCanvas.create_polygon(points, smooth=True, fill="black", outline="white")

def displayAssets():
    counter = 0
    spacing = 100

    for asset in globals.assetListCAD:
        newIcon = AssetIcon(asset, counter)
        globals.assetIcons.append(newIcon)
        if asset.name != "cadCASH":
            counter += 100

    for asset in globals.assetListUSD:
        newIcon = AssetIcon(asset, counter)
        globals.assetIcons.append(newIcon)
        counter += 100


def purchaseProspector(asset):
    global prospectGui
    global prospectAsset
    prospectAsset = asset
    prospectGui = tk.Tk(className="prospector window")

    title = asset.name+" prospector"
    avlbCash = "Current Available Cash"

    global prospectCanvas
    prospectCanvas = tk.Canvas(prospectGui, bg='black', height=720, width=1250)

    prospectCanvas.create_text((500, 150), anchor=W, font=("Impact", 25), text=title, fill="cyan")

    prospectCanvas.create_text((500, 250), anchor=W, font=("Impact", 20), text=avlbCash, fill="cyan")
    prospectCanvas.create_text((560, 275), anchor=W, font=("Impact", 15), text="${0:.2f} CAD".format(globals.totalCash), fill="green")

    global currentAC
    prospectCanvas.create_text((100, 200), anchor=W, font=("Impact", 20), text="average cost set to", fill="white")
    currentAC = prospectCanvas.create_text((140, 225), anchor=W, font=("Impact", 15), text="${0:.2f} CAD".format(asset.averageCost), fill="cyan")
    editACbutton = prospectCanvas.create_text((115, 245), anchor=W, font=("Impact", 10), text="click to edit average cost".format(globals.totalCash), fill="white")
    prospectCanvas.tag_bind(editACbutton, '<ButtonPress-1>', editACclicked)
    prospectCanvas.tag_bind(currentAC, '<ButtonPress-1>', editACclicked)

    prospectGui.geometry("1280x720")
    prospectGui.configure(bg='black')

    bottomframe = Frame(prospectGui, bg='black')
    bottomframe.pack( side = BOTTOM )

    global moneySlider
    moneySlider = Scale(bottomframe, from_=0, to=globals.totalCash, orient=HORIZONTAL, command=sliderChanged, length=1000)
    moneySlider.grid(column=1, row=5, sticky="we")

    global moneyToSpend, averageCost
    moneySpendTitle = prospectCanvas.create_text((550, 380), anchor=W, font=("Impact", 25), text="it would cost", fill="white")
    moneyToSpend = prospectCanvas.create_text((530, 420), anchor=W, font=("Impact", 30), text="$ CAD", fill="green")
    acTitle = prospectCanvas.create_text((460, 460), anchor=W, font=("Impact", 25), text="to reach an average cost of", fill="white")
    averageCost = prospectCanvas.create_text((550, 500), anchor=W, font=("Impact", 30), text="$ CAD", fill="cyan")
    prospectCanvas.create_text((440, 540), anchor=W, font=("Impact", 25), text="at the current market price of", fill="white")
    prospectCanvas.create_text((550, 580), anchor=W, font=("Impact", 30), text="$ {0:.2f} CAD".format(prospectAsset.currentPrice), fill="green")

    prospectCanvas.create_text((330, 655), anchor=W, font=("Impact", 20), text="move slider below to adjust your target average cost", fill="white")

    global bitcoinRatio, ethereumRatio
    if (asset.name == "BTCC-B.TO"):
        bitcoinRatio = speculation.convertBitcoin(asset)
    if (asset.name == "ETHH.TO"):
        ethereumRatio = speculation.convertEthereum(asset)

    moneySlider.pack()

    prospectCanvas.pack()

    prospectGui.mainloop()

def sliderChanged(event):
    global prospectCanvas
    prospectCanvas.itemconfig(moneyToSpend, text="${0:.2f} CAD".format(moneySlider.get()))
    calculation = speculation.calculateAverageCost(prospectAsset, moneySlider.get())
    if (prospectAsset.name == "BTCC-B.TO"):
        prospectCanvas.itemconfig(averageCost, text="${0:.2f} CAD or ${1:.2f} CAD".format(calculation, calculation*bitcoinRatio))
    elif (prospectAsset.name == "ETHH.TO"):
        prospectCanvas.itemconfig(averageCost, text="${0:.2f} CAD or ${1:.2f} CAD".format(calculation, calculation*ethereumRatio))
    else:
        prospectCanvas.itemconfig(averageCost, text="${0:.2f} CAD".format(calculation))

def editACclicked(event):
    master = tk.Tk()
    tk.Label(master, text="New Average Cost").grid(row=0)
    
    global e1
    e1 = tk.Entry(master)
    
    e1.grid(row=0, column=1)
    
    tk.Button(master, text='Quit', command=master.destroy).grid(row=3, column=0, sticky=tk.W, pady=4)
    tk.Button(master, text='Update', command=updateAC).grid(row=3, column=1, sticky=tk.W, pady=4)
    tk.mainloop()

def updateAC():
    global prospectAsset
    prospectAsset.averageCost = float(e1.get())
    prospectCanvas.itemconfig(currentAC, text="${0:.2f} CAD".format(prospectAsset.averageCost))
