from reportlab.pdfgen import canvas
from reportlab.platypus import (SimpleDocTemplate, Paragraph, PageBreak, Image, Spacer, Table, TableStyle)
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER, inch
from reportlab.graphics.shapes import Line, Drawing
from reportlab.lib.colors import Color

import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


class FooterCanvas(canvas.Canvas):

    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []
        self.width, self.height = LETTER

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        page_count = len(self.pages)
        for page in self.pages:
            self.__dict__.update(page)
            if (self._pageNumber > 0):
                self.draw_canvas(page_count)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_canvas(self, page_count):
        page = "Page %s of %s" % (self._pageNumber, page_count)
        x = 128
        self.saveState()
        self.setStrokeColorRGB(0, 0, 0)
        self.setLineWidth(0.5)
        self.setFont('Times-Roman', 10)

        #self.drawImage("logo.png", self.width - inch * 8 - 5, self.height - 50, width=100, height=20, preserveAspectRatio=True)

        self.drawString(self.width - inch * 8 - 5, self.height - 45, "DM2 PASSPORT - PATIENT REPORT")
        self.drawString(self.width - inch * 2.5, self.height - 30, "PATIENT NAME: Robert Grankowski")
        self.drawString(self.width - inch * 2.5, self.height - 45, "DOB: 1984-06-21")

        self.line(30, 740, LETTER[0] - 50, 740)
        self.line(66, 78, LETTER[0] - 66, 78)
        self.setFont('Times-Roman', 10)
        self.drawString(LETTER[0] - x, 65, page)
        self.restoreState()


class PDFReport:

    def __init__(self, path):
        self.path = path

        self.styleSheet = getSampleStyleSheet()
        self.elements = []

        self.colorOhkaGreen0 = Color((45.0 / 255), (166.0 / 255), (153.0 / 255), 1)
        self.colorOhkaGreen1 = Color((182.0 / 255), (227.0 / 255), (166.0 / 255), 1)
        self.colorOhkaGreen2 = Color((140.0 / 255), (222.0 / 255), (192.0 / 255), 1)
        self.colorOhkaBlue0 = Color((54.0 / 255), (122.0 / 255), (179.0 / 255), 1)
        self.colorOhkaBlue1 = Color((122.0 / 255), (180.0 / 255), (225.0 / 255), 1)
        self.colorOhkaGreenLineas = Color((50.0 / 255), (140.0 / 255), (140.0 / 255), 1)

        self.glucoseStatistics()
        self.ambulatoryGlucoseProfile()
        self.bloodPressure()
        self.weight()
        self.medications()

        # Build
        self.doc = SimpleDocTemplate(path, pagesize=LETTER)
        self.doc.multiBuild(self.elements, canvasmaker=FooterCanvas)


    def glucoseStatistics(self):

        psHeaderText = ParagraphStyle('Hed0', fontSize=20, alignment=TA_LEFT, borderWidth=3,
                                      textColor=self.colorOhkaGreen0)
        text = 'GLUCOSE STATISTCS'
        paragraphReportHeader = Paragraph(text, psHeaderText)
        self.elements.append(paragraphReportHeader)

        spacer = Spacer(10, 10)
        self.elements.append(spacer)

        d = Drawing(500, 1)
        line = Line(-15, 0, 483, 0)
        line.strokeColor = self.colorOhkaGreenLineas
        line.strokeWidth = 2
        d.add(line)
        self.elements.append(d)

        spacer = Spacer(10, 1)
        self.elements.append(spacer)

        d = Drawing(500, 1)
        line = Line(-15, 0, 483, 0)
        line.strokeColor = self.colorOhkaGreenLineas
        line.strokeWidth = 0.5
        d.add(line)
        self.elements.append(d)

        spacer = Spacer(10, 22)
        self.elements.append(spacer)

        psHeaderText = ParagraphStyle('Hed0', fontSize=16, alignment=TA_LEFT, borderWidth=3,
                                      textColor=self.colorOhkaBlue0)
        text = 'Average Glucose: 9.8 mmol/L'
        paragraphReportHeader = Paragraph(text, psHeaderText)
        self.elements.append(paragraphReportHeader)

        spacer = Spacer(10, 22)
        self.elements.append(spacer)

        psHeaderText = ParagraphStyle('Hed0', fontSize=16, alignment=TA_LEFT, borderWidth=3,
                                      textColor=self.colorOhkaBlue0)
        text = 'Glucose Variability: 36.9%'
        paragraphReportHeader = Paragraph(text, psHeaderText)
        self.elements.append(paragraphReportHeader)

        spacer = Spacer(10, 55)
        self.elements.append(spacer)

    def ambulatoryGlucoseProfile(self):

        psHeaderText = ParagraphStyle('Hed0', fontSize=20, alignment=TA_LEFT, borderWidth=3,
                                      textColor=self.colorOhkaGreen0)
        text = 'AMBULATORY GLUCOSE PROFILE (AGP)'
        paragraphReportHeader = Paragraph(text, psHeaderText)
        self.elements.append(paragraphReportHeader)

        spacer = Spacer(10, 10)
        self.elements.append(spacer)

        d = Drawing(500, 1)
        line = Line(-15, 0, 483, 0)
        line.strokeColor = self.colorOhkaGreenLineas
        line.strokeWidth = 2
        d.add(line)
        self.elements.append(d)

        spacer = Spacer(10, 1)
        self.elements.append(spacer)

        d = Drawing(500, 1)
        line = Line(-15, 0, 483, 0)
        line.strokeColor = self.colorOhkaGreenLineas
        line.strokeWidth = 0.5
        d.add(line)
        self.elements.append(d)

        spacer = Spacer(10, 22)
        self.elements.append(spacer)

        img = Image('report/glucose_graph.png')
        img.drawHeight = 3.5 * inch
        img.drawWidth = 7 * inch
        self.elements.append(img)

    def bloodPressure(self):

        self.elements.append(PageBreak())

        psHeaderText = ParagraphStyle('Hed0', fontSize=20, alignment=TA_LEFT, borderWidth=3,
                                      textColor=self.colorOhkaGreen0)
        text = 'BLOOD PRESSURE'
        paragraphReportHeader = Paragraph(text, psHeaderText)
        self.elements.append(paragraphReportHeader)

        spacer = Spacer(10, 10)
        self.elements.append(spacer)

        d = Drawing(500, 1)
        line = Line(-15, 0, 483, 0)
        line.strokeColor = self.colorOhkaGreenLineas
        line.strokeWidth = 2
        d.add(line)
        self.elements.append(d)

        spacer = Spacer(10, 1)
        self.elements.append(spacer)

        d = Drawing(500, 1)
        line = Line(-15, 0, 483, 0)
        line.strokeColor = self.colorOhkaGreenLineas
        line.strokeWidth = 0.5
        d.add(line)
        self.elements.append(d)

        spacer = Spacer(10, 22)
        self.elements.append(spacer)

        psHeaderText = ParagraphStyle('Hed0', fontSize=16, alignment=TA_LEFT, borderWidth=3,
                                      textColor=self.colorOhkaBlue0)
        text = 'Systolic Average: 115 mm Hg'
        paragraphReportHeader = Paragraph(text, psHeaderText)
        self.elements.append(paragraphReportHeader)

        spacer = Spacer(10, 22)
        self.elements.append(spacer)

        psHeaderText = ParagraphStyle('Hed0', fontSize=16, alignment=TA_LEFT, borderWidth=3,
                                      textColor=self.colorOhkaBlue0)
        text = 'Diastolic Average: 75 mm Hg'
        paragraphReportHeader = Paragraph(text, psHeaderText)
        self.elements.append(paragraphReportHeader)

        spacer = Spacer(10, 55)
        self.elements.append(spacer)

    def weight(self):
        psHeaderText = ParagraphStyle('Hed0', fontSize=20, alignment=TA_LEFT, borderWidth=3,
                                      textColor=self.colorOhkaGreen0)
        text = 'WEIGHT'
        paragraphReportHeader = Paragraph(text, psHeaderText)
        self.elements.append(paragraphReportHeader)

        spacer = Spacer(10, 10)
        self.elements.append(spacer)

        d = Drawing(500, 1)
        line = Line(-15, 0, 483, 0)
        line.strokeColor = self.colorOhkaGreenLineas
        line.strokeWidth = 2
        d.add(line)
        self.elements.append(d)

        spacer = Spacer(10, 1)
        self.elements.append(spacer)

        d = Drawing(500, 1)
        line = Line(-15, 0, 483, 0)
        line.strokeColor = self.colorOhkaGreenLineas
        line.strokeWidth = 0.5
        d.add(line)
        self.elements.append(d)

        spacer = Spacer(10, 22)
        self.elements.append(spacer)

        psHeaderText = ParagraphStyle('Hed0', fontSize=16, alignment=TA_LEFT, borderWidth=3,
                                      textColor=self.colorOhkaBlue0)
        text = '168 LBS'
        paragraphReportHeader = Paragraph(text, psHeaderText)
        self.elements.append(paragraphReportHeader)

        spacer = Spacer(10, 22)
        self.elements.append(spacer)

    def medications(self):
        self.elements.append(PageBreak())

        psHeaderText = ParagraphStyle('Hed0', fontSize=20, alignment=TA_LEFT, borderWidth=3,
                                      textColor=self.colorOhkaGreen0)
        text = 'MEDICATIONS'
        paragraphReportHeader = Paragraph(text, psHeaderText)
        self.elements.append(paragraphReportHeader)

        spacer = Spacer(10, 10)
        self.elements.append(spacer)

        d = Drawing(500, 1)
        line = Line(-15, 0, 483, 0)
        line.strokeColor = self.colorOhkaGreenLineas
        line.strokeWidth = 2
        d.add(line)
        self.elements.append(d)

        spacer = Spacer(10, 1)
        self.elements.append(spacer)

        d = Drawing(500, 1)
        line = Line(-15, 0, 483, 0)
        line.strokeColor = self.colorOhkaGreenLineas
        line.strokeWidth = 0.5
        d.add(line)
        self.elements.append(d)

        spacer = Spacer(10, 22)
        self.elements.append(spacer)

        psHeaderText = ParagraphStyle('Hed0', fontSize=16, alignment=TA_LEFT, borderWidth=3,
                                      textColor=self.colorOhkaBlue0)
        text = 'CURRENT'
        paragraphReportHeader = Paragraph(text, psHeaderText)
        self.elements.append(paragraphReportHeader)

        spacer = Spacer(10, 22)
        self.elements.append(spacer)

        miglitol_img = Image('media/posts/Miglitol.png')
        miglitol_img.drawHeight = 1 * inch
        miglitol_img.drawWidth = 1 * inch

        tStyle = TableStyle([
            ('SPAN', (0, 0), (-3, -1)),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ALIGN', (1, 0), (1, -1), 'LEFT'),
            ('ALIGN', (2, 0), (2, -1), 'RIGHT'),
            ('LINEABOVE', (0, 1), (-1, -1), 1, self.colorOhkaBlue1),
            ('BACKGROUND', (1, 0), (-1, 0), self.colorOhkaGreen2),

        ])

        lineData = [[miglitol_img, "NAME", "Miglitol"],
                    [" ", "DOSAGE", "50"],
                    [" ", "UNIT", "mg"],
                    [" ", "FREQUENCY", "2 Times Daily"],
                    [" ", "CURRENTLY TAKING", "Yes"],
                    [" ", "START DATE", "2020-10-15"],
                    [" ", "END DATE", "N/A"]]

        table = Table(lineData, colWidths=[250, 125, 125])
        table.setStyle(tStyle)
        self.elements.append(table)

        spacer = Spacer(10, 22)
        self.elements.append(spacer)

        prandin_img = Image('media/posts/Prandin.png')
        prandin_img.drawHeight = 1 * inch
        prandin_img.drawWidth = 1 * inch

        tStyle = TableStyle([
            ('SPAN', (0, 0), (-3, -1)),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ALIGN', (1, 0), (1, -1), 'LEFT'),
            ('ALIGN', (2, 0), (2, -1), 'RIGHT'),
            ('LINEABOVE', (0, 1), (-1, -1), 1, self.colorOhkaBlue1),
            ('BACKGROUND', (1, 0), (-1, 0), self.colorOhkaGreen2),

        ])

        lineData = [[prandin_img, "NAME", "Prandin"],
                    [" ", "DOSAGE", "2"],
                    [" ", "UNIT", "mg"],
                    [" ", "FREQUENCY", "1 Time Daily"],
                    [" ", "CURRENTLY TAKING", "Yes"],
                    [" ", "START DATE", "2021-01-01"],
                    [" ", "END DATE", "N/A"]]

        table = Table(lineData, colWidths=[250, 125, 125])
        table.setStyle(tStyle)
        self.elements.append(table)

        spacer = Spacer(10, 22)
        self.elements.append(spacer)

        psHeaderText = ParagraphStyle('Hed0', fontSize=16, alignment=TA_LEFT, borderWidth=3,
                                      textColor=self.colorOhkaBlue0)
        text = 'HISTORICAL'
        paragraphReportHeader = Paragraph(text, psHeaderText)
        self.elements.append(paragraphReportHeader)

        spacer = Spacer(10, 22)
        self.elements.append(spacer)

        tStyle = TableStyle([
            ('SPAN', (0, 0), (-3, -1)),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ALIGN', (1, 0), (1, -1), 'LEFT'),
            ('ALIGN', (2, 0), (2, -1), 'RIGHT'),
            ('LINEABOVE', (0, 1), (-1, -1), 1, self.colorOhkaBlue1),
            ('BACKGROUND', (1, 0), (-1, 0), self.colorOhkaGreen2),

        ])

        lineData = [[" ", "NAME", "Acarbose (Precose)"],
                    [" ", "DOSAGE", "10"],
                    [" ", "UNIT", "mg"],
                    [" ", "FREQUENCY", "3 Times Daily"],
                    [" ", "CURRENTLY TAKING", "NO"],
                    [" ", "START DATE", "2020-09-09"],
                    [" ", "END DATE", "2021-03-31"]]

        table = Table(lineData, colWidths=[250, 125, 125])
        table.setStyle(tStyle)
        self.elements.append(table)


def glucose_graph(df):

    df['glucose_reading'] = df['glucose_reading'].astype('float')
    df['date'] = df['date'].astype('str')
    df['time'] = df['time'].astype('str')

    df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'])

    sns.set(style='whitegrid', palette="deep", font_scale=1.1, rc={"figure.figsize": [8, 5]})

    fig, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
    ax1.plot(df.datetime,
             df.glucose_reading,
             color="black",
             linestyle='solid', marker="o")
    ax1.set_xlabel('Date', fontsize=18)
    ax1.set_ylabel('Glucose Readings (mmol/L)', fontsize=18)

    for tick in ax1.get_xticklabels():
        tick.set_rotation(35)

    ax1.axhspan(0, 3, facecolor='red', alpha=0.4)
    ax1.axhspan(3, 3.9, facecolor='yellow', alpha=0.4)
    ax1.axhspan(3.9, 10, facecolor='#01FF49', alpha=0.4)
    ax1.axhspan(10, 13.9, facecolor='yellow', alpha=0.4)
    ax1.axhspan(13.9, 16, facecolor='red', alpha=0.4)

    plt.savefig('report/glucose_graph.png')
