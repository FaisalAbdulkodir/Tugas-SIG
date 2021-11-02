import shapefile

w=shapefile.Writer('soal0',shapeType=shapefile.POLYGON)
w.shapeType

w.field("kolom1","C")


w.record("ngek","satu")


w.poly([[[-5,5],[5,5], [10,-5],[-5,-5], [-5,5]]])