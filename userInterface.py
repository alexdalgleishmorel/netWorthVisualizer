import tkinter as tk
from tkinter import *
import globals as globals

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


        self.box = round_rectangle(100, 225+counter, 1170, 275+counter)
        self.xRange = (100, 1170)
        self.yRange = (225+counter, 275+counter)
        print("y range for {0} is {1} - {2}".format(asset.name, 225+counter, 275+counter))
        self.name = menuCanvas.create_text(175, 250+counter, font=("Impact", 25), text=asset.name, fill="white")
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
        print(event)
        self.asset.showHistory()

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

def createMenu(initialize):
    if initialize:
        global menuGui, gameSize, playType
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
    menuCanvas.create_text((450, 150), anchor=W, font=("Impact", 50), text="${:.2f} CAD".format(globals.netWorth), fill="green")
    menuCanvas.create_text((1100, 20), anchor=W, font=("Impact", 10), text=scrollInstruct, fill="grey")


    displayAssets()

    frame.pack()
    menuGui.mainloop()

"""

def iconClick(event):
    print(event)
    for assetIcon in globals.assetIcons:
        if assetIcon.clicked(event.x, event.y):
            assetIcon.asset.showHistory()

"""

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
        counter += 100

    for asset in globals.assetListUSD:
        newIcon = AssetIcon(asset, counter)
        globals.assetIcons.append(newIcon)
        counter += 100