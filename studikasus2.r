# Memuat library yang diperlukan
library(ggplot2)

# Mendefinisikan data
fakultas <- c("Bisnis", "D3 Perhotelan", "ICT", "Ilmu Komunikasi", "Seni dan Desain")
jumlah_mahasiswa <- c(260, 28, 284, 465, 735)
akreditasi <- c("A","A","B","A","A")

# Membuat sebuah data frame
info_mahasiswa <- data.frame(fakultas, jumlah_mahasiswa, akreditasi)

# Menampilkan data frame
print(info_mahasiswa)


# Membuat plot
gambar <- ggplot(info_mahasiswa, aes(x=fakultas, y=jumlah_mahasiswa, fill=fakultas)) +
  geom_bar(width=1, stat="identity") +
  labs(y = "jumlah_mahasiswa", fill = "fakultas") +
  theme_minimal()+
  theme(panel.background = element_rect(fill = "grey", colour = "grey"))

# Menampilkan plot
print(gambar)