import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
fic = "autos.xls"
df = pd.read_excel(fic)
df_num = df.select_dtypes(include="number")
print(df)

corr_depart = df_num.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_depart, annot=False, vmin=-1, vmax=1, cmap="coolwarm")
plt.title("Matrice de corrélation - données brutes")
plt.tight_layout()
plt.show()

# centrage-réduction "à la main"
df_cr = (df_num - df_num.mean()) / df_num.std(ddof=0)

corr_cr = df_cr.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_cr, annot=False, vmin=-1, vmax=1, cmap="coolwarm")
plt.title("Matrice de corrélation - données centrées-réduites")
plt.tight_layout()
plt.show()


cov_depart = df_num.cov()

plt.figure(figsize=(8, 6))
sns.heatmap(cov_depart, annot=False, cmap="viridis")
plt.title("Matrice de variance-covariance - données brutes")
plt.tight_layout()
plt.show()

