#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ddalpha
Version  : 1.3.3
Release  : 13
URL      : https://cran.r-project.org/src/contrib/ddalpha_1.3.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ddalpha_1.3.3.tar.gz
Summary  : Depth-Based Classification and Calculation of Data Depth
Group    : Development/Tools
License  : GPL-2.0
Requires: R-ddalpha-lib
Requires: R-BH
Requires: R-Rcpp
Requires: R-geometry
Requires: R-robustbase
Requires: R-sfsmisc
BuildRequires : R-BH
BuildRequires : R-Rcpp
BuildRequires : R-geometry
BuildRequires : R-robustbase
BuildRequires : R-sfsmisc
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-ddalpha package.
Group: Libraries

%description lib
lib components for the R-ddalpha package.


%prep
%setup -q -c -n ddalpha

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1525363846

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1525363846
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ddalpha
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ddalpha
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ddalpha
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library ddalpha|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ddalpha/CITATION
/usr/lib64/R/library/ddalpha/DESCRIPTION
/usr/lib64/R/library/ddalpha/INDEX
/usr/lib64/R/library/ddalpha/Meta/Rd.rds
/usr/lib64/R/library/ddalpha/Meta/data.rds
/usr/lib64/R/library/ddalpha/Meta/features.rds
/usr/lib64/R/library/ddalpha/Meta/hsearch.rds
/usr/lib64/R/library/ddalpha/Meta/links.rds
/usr/lib64/R/library/ddalpha/Meta/nsInfo.rds
/usr/lib64/R/library/ddalpha/Meta/package.rds
/usr/lib64/R/library/ddalpha/NAMESPACE
/usr/lib64/R/library/ddalpha/R/ddalpha
/usr/lib64/R/library/ddalpha/R/ddalpha.rdb
/usr/lib64/R/library/ddalpha/R/ddalpha.rdx
/usr/lib64/R/library/ddalpha/data/baby.txt.gz
/usr/lib64/R/library/ddalpha/data/banknoten.txt.gz
/usr/lib64/R/library/ddalpha/data/biomed.txt.gz
/usr/lib64/R/library/ddalpha/data/bloodtransfusion.txt.gz
/usr/lib64/R/library/ddalpha/data/breast_cancer_wisconsin.txt.gz
/usr/lib64/R/library/ddalpha/data/bupa.txt.gz
/usr/lib64/R/library/ddalpha/data/chemdiab_1vs2.txt.gz
/usr/lib64/R/library/ddalpha/data/chemdiab_1vs3.txt.gz
/usr/lib64/R/library/ddalpha/data/chemdiab_2vs3.txt.gz
/usr/lib64/R/library/ddalpha/data/cloud.txt.gz
/usr/lib64/R/library/ddalpha/data/crabB_MvsF.txt.gz
/usr/lib64/R/library/ddalpha/data/crabF_BvsO.txt.gz
/usr/lib64/R/library/ddalpha/data/crabM_BvsO.txt.gz
/usr/lib64/R/library/ddalpha/data/crabO_MvsF.txt.gz
/usr/lib64/R/library/ddalpha/data/crab_BvsO.txt.gz
/usr/lib64/R/library/ddalpha/data/crab_MvsF.txt.gz
/usr/lib64/R/library/ddalpha/data/cricket_CvsP.txt.gz
/usr/lib64/R/library/ddalpha/data/diabetes.txt.gz
/usr/lib64/R/library/ddalpha/data/ecoli_cpvsim.txt.gz
/usr/lib64/R/library/ddalpha/data/ecoli_cpvspp.txt.gz
/usr/lib64/R/library/ddalpha/data/ecoli_imvspp.txt.gz
/usr/lib64/R/library/ddalpha/data/gemsen_MvsF.txt.gz
/usr/lib64/R/library/ddalpha/data/geneexp.rda
/usr/lib64/R/library/ddalpha/data/glass.txt.gz
/usr/lib64/R/library/ddalpha/data/groessen_MvsF.txt.gz
/usr/lib64/R/library/ddalpha/data/growth.rda
/usr/lib64/R/library/ddalpha/data/haberman.txt.gz
/usr/lib64/R/library/ddalpha/data/heart.txt.gz
/usr/lib64/R/library/ddalpha/data/hemophilia.txt.gz
/usr/lib64/R/library/ddalpha/data/indian_liver_patient_1vs2.txt.gz
/usr/lib64/R/library/ddalpha/data/indian_liver_patient_FvsM.txt.gz
/usr/lib64/R/library/ddalpha/data/iris_setosavsversicolor.txt.gz
/usr/lib64/R/library/ddalpha/data/iris_setosavsvirginica.txt.gz
/usr/lib64/R/library/ddalpha/data/iris_versicolorvsvirginica.txt.gz
/usr/lib64/R/library/ddalpha/data/irish_ed_MvsF.txt.gz
/usr/lib64/R/library/ddalpha/data/kidney.txt.gz
/usr/lib64/R/library/ddalpha/data/medflies.rda
/usr/lib64/R/library/ddalpha/data/pima.txt.gz
/usr/lib64/R/library/ddalpha/data/plasma_retinol_MvsF.txt.gz
/usr/lib64/R/library/ddalpha/data/population.rda
/usr/lib64/R/library/ddalpha/data/population2010.rda
/usr/lib64/R/library/ddalpha/data/segmentation.txt.gz
/usr/lib64/R/library/ddalpha/data/socmob_IvsNI.txt.gz
/usr/lib64/R/library/ddalpha/data/socmob_WvsB.txt.gz
/usr/lib64/R/library/ddalpha/data/tae.txt.gz
/usr/lib64/R/library/ddalpha/data/tecator.rda
/usr/lib64/R/library/ddalpha/data/tennis_MvsF.txt.gz
/usr/lib64/R/library/ddalpha/data/tips_DvsN.txt.gz
/usr/lib64/R/library/ddalpha/data/tips_MvsF.txt.gz
/usr/lib64/R/library/ddalpha/data/uscrime_SvsN.txt.gz
/usr/lib64/R/library/ddalpha/data/vertebral_column.txt.gz
/usr/lib64/R/library/ddalpha/data/veteran_lung_cancer.txt.gz
/usr/lib64/R/library/ddalpha/data/vowel_MvsF.txt.gz
/usr/lib64/R/library/ddalpha/data/wine_1vs2.txt.gz
/usr/lib64/R/library/ddalpha/data/wine_1vs3.txt.gz
/usr/lib64/R/library/ddalpha/data/wine_2vs3.txt.gz
/usr/lib64/R/library/ddalpha/help/AnIndex
/usr/lib64/R/library/ddalpha/help/aliases.rds
/usr/lib64/R/library/ddalpha/help/ddalpha.rdb
/usr/lib64/R/library/ddalpha/help/ddalpha.rdx
/usr/lib64/R/library/ddalpha/help/paths.rds
/usr/lib64/R/library/ddalpha/html/00Index.html
/usr/lib64/R/library/ddalpha/html/R.css
/usr/lib64/R/library/ddalpha/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/ddalpha/libs/ddalpha.so
/usr/lib64/R/library/ddalpha/libs/ddalpha.so.avx2
/usr/lib64/R/library/ddalpha/libs/ddalpha.so.avx512
