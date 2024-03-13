import { Album } from "./module";

export const ALBUMS: Album[] = [];

for (let i : number = 0; i < 5; i++){
    ALBUMS.push(
        {
            id: i+1,
            title: `title ${i+1}`,
        }
        
    )
}