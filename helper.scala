
def binN(n: Int): List[String] = {
  n match {
    case 1 => List("0", "1")
	case m => for {
	  a <- List("0", "1")
      b <- binN(m-1)
    } yield a+b
  }
}  

def addE(s: String): List[String] = (s.toCharArray ++ "e").permutations.toList.map(_.mkString)

val e3 = binN(2).flatMap(addE).map(_.mkString).toSet

val pairs = (1 to 4).combinations(2).toList

val b2 = binN(2)

val prod = for { b <- b2; p <- pairs } yield (b, p)

val ls = prod.map { case (pattern, place) =>
  e4.filter( s => s(place(0)-1) == pattern(0) &&
                  s(place(1)-1) == pattern(1))
				  
}

val in = ls.map( set => s"""square(${set.map("E"+_).mkString(", ")})""")

in.mkString(",\n")


val p5 = (1 to 5).combinations(3).toList
val b3 = binN(3)

val e5 = b4.flatMap(addE).map(_.mkString).toSet
val prod = for { b <- b4; p <- p5 } yield (b, p)

val ls = prod.map { case (pattern, place) =>
  e5.filter( s => s(place(0)-1) == pattern(0) &&
                  s(place(1)-1) == pattern(1) && 
				  s(place(2)-1) == pattern(2))				  
}

val in = ls.map( set => s"""square(${set.map("E"+_).mkString(", ")})""")
val a= in.mkString(",\n")

val w = new BufferedWriter(new FileWriter("a5.txt"))
w.write(a)

w.close
w.write(b)

val pairs = (1 to 4).combinations(2).toList
val triples = (1 to 4).combinations(3).toList

val b3 = binN(3)
val e4 = b3.flatMap(addE).map(_.mkString).toSet

val prod = for { b <- b3; p <- triples } yield (b, p)

val ls = prod.map { case (pattern, place) =>
  e4.filter( s => s(place(0)-1) == 'e' ||
                  s(place(1)-1) == 'e' || 
				  s(place(2)-1) == 'e')				  
}

val in = ls.map( set => s"""cube(${set.map("E"+_).mkString(", ")})""")

val a = in.mkString(",\n")

