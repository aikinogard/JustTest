SUBROUTINE f2loops(f, g, out, n, m, p)
	IMPLICIT NONE
	INTEGER, PARAMETER :: dp = selected_real_kind(15, 307)
	INTEGER :: n, m, p, i, j
	REAL(dp) :: f(n,p), g(m,p), out(n,m)

	!F2PY REAL(dp), INTENT(in), DIMENSION(n,p) :: f
	!F2PY REAL(dp), INTENT(in), DIMENSION(m,p) :: g
	!F2PY REAL(dp), INTENT(out), DIMENSION(n,m) :: out
	!F2PY INTEGER, INTENT(in) :: n, m, p

	DO i = 1, n
		DO j = 1, m
			out(i, j) = EXP(-SQRT(SUM((f(i, :) - g(j, :))**2)))
		END DO
	END DO
END SUBROUTINE f2loops

SUBROUTINE f4loops(f, g, out, n, m, p)
	IMPLICIT NONE
	INTEGER, PARAMETER :: dp = selected_real_kind(15, 307)
	INTEGER :: n, m, p, i, j, k, l
	REAL(dp) :: f(n,p), g(m,p), out(n,m,p,p)
	
	!F2PY REAL(dp), INTENT(in), DIMENSION(n,p) :: f
	!F2PY REAL(dp), INTENT(in), DIMENSION(m,p) :: g
	!F2PY REAL(dp), INTENT(out), DIMENSION(n,m,p,p) :: out
	!F2PY INTEGER, INTENT(in) :: n, m, p
	
	DO i = 1, n
		DO j = 1, m
			DO k = 1, p
				DO l = 1, p
					out(i,j,k,l) = EXP(-(f(i, k) - g(j, l))**2)
				END DO
			END DO
		END DO
	END DO
	
END SUBROUTINE f4loops

